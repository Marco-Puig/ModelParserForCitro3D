# Parser code
def parse_obj_to_c_array(obj_file_path, output_c_file_path):
    with open(obj_file_path, "r") as file:
        obj_data = file.read()

    # Layout
    vertices = []
    texcoords = []
    normals = []
    faces = []

    # Parse/iterate through the file and map to the layout (store in lists)
    for line in obj_data.splitlines():
        if line.startswith("v "):
            parts = list(map(float, line.strip().split()[1:]))
            vertices.append(parts)
        elif line.startswith("vt "):
            parts = list(map(float, line.strip().split()[1:]))
            texcoords.append(parts)
        elif line.startswith("vn "):
            parts = list(map(float, line.strip().split()[1:]))
            normals.append(parts)
        elif line.startswith("f "):
            parts = line.strip().split()[1:]
            face = []
            for part in parts:
                indices = part.split('/')
                v_idx = int(indices[0]) if len(indices) > 0 and indices[0] else 0
                vt_idx = int(indices[1]) if len(indices) > 1 and indices[1] else 0
                vn_idx = int(indices[2]) if len(indices) > 2 and indices[2] else 0
                face.append((v_idx, vt_idx, vn_idx))
            faces.append(face)

    # Take that layout and format it to .c code
    def format_vertex(v_idx, vt_idx, vn_idx):
        v = vertices[v_idx - 1]
        vt = texcoords[vt_idx - 1] if vt_idx else [0.0, 0.0]
        vn = normals[vn_idx - 1] if vn_idx else [0.0, 0.0, 0.0]
        return f"{{ {{{v[0]:+.6f}f, {v[1]:+.6f}f, {v[2]:+.6f}f}}, " \
               f"{{{vt[0]:.6f}f, {vt[1]:.6f}f}}, " \
               f"{{{vn[0]:+.6f}f, {vn[1]:+.6f}f, {vn[2]:+.6f}f}} }}"

    # Add the vertex_list code snippet and write to a .c file
    vertex_list_code = ["static const vertex vertex_list[] =\n{"]
    for face in faces:
        for v in face:
            vertex_line = format_vertex(*v)
            vertex_list_code.append(f"\t{vertex_line},")
    vertex_list_code.append("};")

    # Write to output file
    with open(output_c_file_path, "w") as f:
        f.write("\n".join(vertex_list_code))
    print(f"C vertex array written to: {output_c_file_path}")

# Run the program :)
model_path = input("Please provide the path your model is in. If it in the same path as this program, simply type in the model name:")
try:
  parse_obj_to_c_array(model_path, "model_code.c")
except FileNotFoundError:
  print("Model not found. Be sure to list the correct file path as well as your model name.")
except Exception as e:
  print(f"An error occurred: {e}")