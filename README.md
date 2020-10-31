# Pygame 3D Test

A simple project that shows off basic 3D rendering in Pygame.

| Cube                      | Tetrahedron                      |
| ------------------------- | -------------------------------- |
| ![](screenshots/cube.png) | ![](screenshots/tetrahedron.png) |

| Octahedron                      | Icosahedron                      |
| ------------------------------- | -------------------------------- |
| ![](screenshots/octahedron.png) | ![](screenshots/icosahedron.png) |

### Requirements

You'll need Python 3 with Pygame, NumPy and SciPy installed.

You can install the required packages via:

```
pip install -r requirements.txt
```

### Basic usage

To run the example:

```
python main.py
```

Use the arrow keys :arrow_up: :arrow_down: :arrow_left: :arrow_right: or mouse to rotate 3D object.

You can change the 3D object by modifying the following line in `main.py`:

```python
poly = polyhedron.create_cube()
```

Here are some additional 3D objects already implemented:
```python
polyhedron.create_tetrahedron()
polyhedron.create_octahedron()
polyhedron.create_icosahedron()
```

### Cool features to implement

Here are some cool features that might be worth implementing.

* Perspective projections
* Shading / solid body
* 3D animations / transformations
