# Model Parser for Citro3D/devkitPro
Model Parser for Citro3D/devkitPro is a Python program that converts an Obj to .c code that can be used for Citro3D/devkitPro

Model in Blender             |  Model being rendered via Citro3D 
:-------------------------:|:-------------------------:
<img width="337" alt="exampleBlender" src="https://github.com/user-attachments/assets/7763154b-0818-407b-b423-796f7fd6bca9" /> | <img width="300" alt="example3ds" src="https://github.com/user-attachments/assets/6c63945e-4f16-41bd-a648-52280b7a87c6" />

## Please Read the Following to Understand the process of prepping your model before converting it into a ``vertex_list``:

In order to generate an accurate output like:

```{ {x, y, z}, {u, v}, {nx, ny, nz} }```

### Please use the Blender Export Settings:

1. Go to `File` → `Export` → `Wavefront (.obj)`

2. In the **export options panel** on the left:
     ### Check:
   * ✔️ **Selection Only** (optional: only if you want to export only selected object)
   * ✔️ **Include Normals**
   * ✔️ **Include UVs**
   * ❌ **Write Materials** *(optional — disable if you don’t need `.mtl` files)*
   * ✔️ **Triangulate Faces** → **Enabled** *(important to match triangle-based rendering)*
   * ✔️ **Include Edges** *(optional — not used in most rendering)*
   * ✔️ **Objects as OBJ Objects** *(recommended for single model)*
   * ✔️ **Apply Modifiers** *(recommended if you've used modifiers like Subdivision Surface)*
   ### Change:
   * ⚠️ **Forward Axis:** usually set to `-Z Forward`
   * ⚠️ **Up Axis:** usually `Y Up`

---
### Additional Warnings:

* If your model doesn’t have UVs yet, unwrap it first in Blender (`Tab` → Edit Mode → `U` → Unwrap).
* If your model is smooth-shaded, know that the export will work, but the final model may not carry such properties over.
---

### Result in `.obj`

A correctly exported `.obj` will contain something such as this:

```plaintext
static const vertex vertex_list[] =
{
	{ {+0.000000f, -0.668544f, +0.000000f}, {0.181819f, 0.000000f}, {-0.017500f, -0.999600f, +0.024300f} },
	{ {+0.425323f, -0.668475f, +0.309011f}, {0.227273f, 0.078731f}, {-0.017500f, -0.999600f, +0.024300f} },
	{ {-0.162456f, -0.653558f, +0.499995f}, {0.136365f, 0.078731f}, {-0.017500f, -0.999600f, +0.024300f} },
	{ {+0.723607f, -0.447220f, +0.525725f}, {0.272728f, 0.157461f}, {+0.402600f, -0.857200f, +0.321100f} },
	{ {+0.425323f, -0.668475f, +0.309011f}, {0.318182f, 0.078731f}, {+0.402600f, -0.857200f, +0.321100f} },
	{ {+0.975733f, -0.525736f, +0.000000f}, {0.363637f, 0.157461f}, {+0.402600f, -0.857200f, +0.321100f} },
	{ {+0.000000f, -0.668544f, +0.000000f}, {0.909091f, 0.000000f}, {-0.103700f, -0.994600f, -0.003900f} },
	{ {-0.162456f, -0.653558f, +0.499995f}, {0.954545f, 0.078731f}, {-0.103700f, -0.994600f, -0.003900f} },
	{ {-0.525730f, -0.613727f, +0.000000f}, {0.863636f, 0.078731f}, {-0.103700f, -0.994600f, -0.003900f} },
	{ {+0.000000f, -0.668544f, +0.000000f}, {0.727273f, 0.000000f}, {-0.103700f, -0.994100f, -0.032100f} },
	{ {-0.525730f, -0.613727f, +0.000000f}, {0.772727f, 0.078731f}, {-0.103700f, -0.994100f, -0.032100f} },
	
	{ {-0.162456f, -0.635469f, -0.499995f}, {0.681818f, 0.078731f}, {-0.103700f, -0.994100f, -0.032100f} },
	{ {+0.000000f, -0.668544f, +0.000000f}, {0.545455f, 0.000000f}, {+0.013000f, -0.997400f, -0.070200f} },
	{ {-0.162456f, -0.635469f, -0.499995f}, {0.590909f, 0.078731f}, {+0.013000f, -0.997400f, -0.070200f} },
	{ {+0.425323f, -0.641274f, -0.309011f}, {0.500000f, 0.078731f}, {+0.013000f, -0.997400f, -0.070200f} },
	{ {+0.723607f, -0.447220f, +0.525725f}, {0.272728f, 0.157461f}, {+0.832200f, -0.326900f, +0.447900f} },
	{ {+0.975733f, -0.525736f, +0.000000f}, {0.363637f, 0.157461f}, {+0.832200f, -0.326900f, +0.447900f} },
	{ {+1.015939f, +0.000000f, +0.309013f}, {0.318182f, 0.236191f}, {+0.832200f, -0.326900f, +0.447900f} },
};
```
