import numpy as np
import pyvista as pv
import pyvistaqt as pvqt
from PySide6.QtWidgets import QStackedLayout, QWidget


class GeometryWidget(QWidget):
    colors = []
    default_color = [179, 204, 204]  # gray/blueish
    select_color = [255, 0, 0]  # red

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.actors = []
        self.points_poly = None
        self.points_actor = None
        self.points = None
        self.selected_nodes = None
        self.line_nodes = None
        self.face_nodes = None
        self.plotter = None
        self.parent = parent
        self.layout = QStackedLayout()
        self.setLayout(self.layout)
        self.connector = ""

    def setup(self):
        self.selected_nodes = []
        self.line_nodes = []
        self.face_nodes = []
        self.plotter = pvqt.QtInteractor(self)
        self.layout.addWidget(self.plotter.interactor)

    def create_nodes(self, points):
        self.points = points
        self.points_poly = pv.PolyData(points)

        self.colors = np.full(
            (len(self.points), 3), self.default_color, dtype=np.uint8
        )
        self.points_poly["colors"] = self.colors

        self.points_actor = self.plotter.add_points(
            self.points_poly,
            render_points_as_spheres=True,
            point_size=20,
            scalars="colors",
            rgb=True,
        )
        self.plotter.show_grid()
        self.plotter.add_point_labels(
            points,
            range(1, len(self.points) + 1),  # Automatically labels each point
            # with its index
            font_size=15,
            point_color="white",
            text_color="black",
            always_visible=True,
        )
        self.plotter.show()

    def change_connector(self, connector):
        self.connector = connector
        if self.plotter is not None:
            self.plotter.disable_picking()
            if self.connector == "delete":
                self.plotter.enable_mesh_picking(
                    self.mesh_callback,
                    show_message="Right Click to select",
                )
            else:
                self.plotter.enable_surface_point_picking(
                    self.point_callback,
                    show_message="Right Click to select",
                    clear_on_no_selection=False,
                )

    def mesh_callback(self, poly_data):
        picked_actor = self.plotter.picked_actor
        if picked_actor in self.actors:
            self.plotter.remove_actor(picked_actor)
            self.actors.remove(picked_actor)
            self.plotter.render()
            if poly_data.lines.size > 0:
                line = []
                for i in range(poly_data.points.shape[0]):
                    line.append(
                        self.points_poly.find_closest_point(
                            poly_data.points[i]
                        )
                    )
                for arr in self.line_nodes:
                    if np.array_equal(arr, line):
                        self.line_nodes.remove(arr)
                        break
            elif poly_data.faces.size > 0:
                faces = poly_data.faces[1:]
                for arr in self.face_nodes:
                    if np.array_equal(arr, faces):
                        self.face_nodes.remove(arr)
                        break

    def point_callback(self, point):
        point_idx = self.points_poly.find_closest_point(point)
        if point_idx not in self.selected_nodes:
            self.colors[point_idx] = self.select_color
            self.selected_nodes.append(point_idx)
        else:
            self.colors[point_idx] = self.default_color
            self.selected_nodes.remove(point_idx)
        self.points_poly["colors"] = self.colors  # Refresh
        self.check_connections()

    def check_connections(self):
        nodes = None
        match self.connector:
            case "line":
                if len(self.selected_nodes) == 2:
                    nodes = self.selected_nodes.copy()
                    self.line_nodes.append(nodes)
                    self.selected_nodes.clear()
                elif len(self.selected_nodes) > 2:
                    raise ValueError("Too many nodes")
            case "tri":
                if len(self.selected_nodes) == 3:
                    nodes = self.selected_nodes.copy()
                    self.face_nodes.append(nodes)
                    self.selected_nodes.clear()
                elif len(self.selected_nodes) > 3:
                    raise ValueError("Too many nodes")
            case "quad":
                if len(self.selected_nodes) == 4:
                    nodes = self.selected_nodes.copy()
                    self.face_nodes.append(nodes)
                    self.selected_nodes.clear()
                elif len(self.selected_nodes) > 4:
                    raise ValueError("Too many nodes")
        if nodes:
            self.reset_colors()
            self.update_geometry(nodes)

    def update_geometry(self, nodes):
        actor = None
        if len(nodes) == 2:
            line = pv.Line(
                self.points_poly.points[nodes[0]],
                self.points_poly.points[nodes[1]],
            )
            actor = self.plotter.add_mesh(line, line_width=6, color="k")
        if len(nodes) > 2:
            face = [len(nodes)]
            face.extend(nodes)
            poly_data = pv.PolyData(self.points_poly.points, face)
            actor = self.plotter.add_mesh(poly_data)
        self.actors.append(actor)

    def reset_colors(self):
        for i in range(len(self.colors)):
            self.colors[i] = self.default_color
        self.points_poly["colors"] = self.colors  # Refresh

    def clear(self):
        if self.plotter:
            self.layout.removeWidget(self.plotter)  # removes from layout
            self.plotter.setParent(None)  # detaches it from the parent widget
            self.plotter.deleteLater()  # schedules cleanup

    def update_points(self, points):
        self.points_poly.points = points

        for actor in self.actors:
            self.plotter.remove_actor(actor)
            self.actors.remove(actor)
        self.redraw()
        self.plotter.render()

    def redraw(self):
        for line in self.line_nodes:
            self.update_geometry(line)
        for face in self.face_nodes:
            self.update_geometry(face)
