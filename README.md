# Atomic Atlas

Atomic Atlas is a Python/Pygame educational periodic-table application. It presents element data, atomic details, isotope information, and related images in an interactive desktop window. A second application variant includes a simple notes browser and editor.

The project also includes a Pillow-based script for generating custom atom illustrations.

## Features

- Interactive periodic table layout.
- Element detail view with:
  - Name and symbol.
  - Atomic number and atomic weight.
  - Category and state at room temperature.
  - Isotope names.
  - Element and isotope images when available.
- General notes and per-element notes in the notes-enabled application.
- Basic text editing for Markdown notes.
- Custom atom image generation with configurable proton, neutron, and electron counts.

## Requirements

- Windows, macOS, or Linux.
- Python 3.10 or newer is recommended.
- `pygame` for the desktop application.
- `Pillow` for atom image generation.

The existing `requirements.py` file is empty, so install the packages directly:

```powershell
python -m pip install pygame Pillow
```

## Installation

From the project root:

```powershell
cd AtomicAtlas
python -m venv venv
.\venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install pygame Pillow
```

On macOS or Linux, activate the virtual environment with:

```bash
source venv/bin/activate
```

The application reads `.config` using a relative path, so run the commands below from the project root unless stated otherwise.

## Running the Application

### Basic periodic table

```powershell
python main.py
```

Click an element to open its details. Click **Back** to return to the table. Close the Pygame window to exit.

### Notes-enabled version

```powershell
python test.py
```

This version includes the same periodic-table and element-detail workflow, plus:

- A **Notes** button for general notes.
- A **Notes** button in an element detail view for notes belonging to that element.
- Existing Markdown note files can be opened and edited.
- **+ New Note** creates a new Markdown note.
- Press `Esc` while editing to save and return.
- Press `Esc` in a notes list to return to the previous view.

`test.py` is the notes-enabled application, not an automated test suite.

## Generating Atom Images

The generator is located at `images/generate.py`. Run it from the `images` directory:

```powershell
cd images
python generate.py
```

With no arguments, it generates an atom using the defaults:

- 1 proton
- 0 neutrons
- 1 electron

Supply optional positional arguments in this order:

```powershell
python generate.py <protons> <neutrons> <electrons>
```

For example, to generate a carbon-like atom:

```powershell
python generate.py 6 6 6
```

Partial arguments are supported. Missing values use their defaults:

```powershell
python generate.py 2
python generate.py 2 2
```

The generated image is saved as `images/atom.png` and is also opened using the operating system's default image viewer. The image includes a transparent background, a nucleus, electron shells, electrons, and text showing the proton, electron, and neutron counts.

## Project Structure

```text
AtomicAtlas/
├── .config                  # Application name, version, and data paths
├── AtomicAtlas.code-workspace
├── main.py                  # Basic periodic-table application
├── test.py                  # Notes-enabled application variant
├── periodic_table_data.py   # Element data, positions, colors, and image paths
├── requirements.py          # Currently empty; dependencies are listed above
├── run.bat                  # Windows launcher template with an old absolute path
├── images/
│   ├── generate.py          # Custom atom image generator
│   ├── atom.png            # Generated atom image
│   ├── alpha.png           # Alpha radiation icon
│   ├── beta.png            # Beta radiation icon
│   ├── gamma.png           # Gamma radiation icon
│   ├── Unstable.png        # Unstable-isotope icon
│   └── <element>/           # Element and isotope images
├── notes/
│   ├── general.md          # General notes
│   ├── buildnotes/         # Development notes
│   └── <element>/           # Per-element notes created by the app
└── data/                    # Reserved for additional project data
```

## Data and Images

Element definitions are stored in `periodic_table_data.py`. Each element record contains its display name, symbol, atomic number, atomic weight, category, state, isotopes, screen position, colors, description, and image paths.

Image paths are relative to the project root, for example:

```text
images/C/C.png
images/C/C-12.png
```

When adding an element image, update the corresponding entry in `periodic_table_data.py` and ensure the referenced file exists.

## Configuration

The `.config` file currently stores:

- Application name.
- Application version.
- Developer name.
- Image and notes directory settings.

Both GUI scripts read the version from this file. Keep the working directory at the project root when launching `main.py` or `test.py` so `.config` and the relative image paths resolve correctly.

## Windows Launcher Note

`run.bat` contains a hardcoded path from an older machine:

```text
C:\Users\noax0579\Desktop\AtomicAtlas\
```

It will need to be updated for the current computer before it can be used. The reliable alternative is to activate the virtual environment and run `python main.py` or `python test.py` from the project root.

## Development Notes

- The GUI uses a fixed window size of 1300 by 600 pixels.
- The project currently has no automated test suite.
- `pygame` opens a desktop window, so GUI runs require a graphical environment.
- The generator accepts integer command-line values but does not currently validate whether they are physically meaningful or non-negative.
- Some elements have incomplete descriptions or missing images; the application displays available data and reports missing image paths in the console.

## License

No license file is currently included in the repository.
