from PIL import Image, ImageDraw, ImageFont
import argparse
import math
from pathlib import Path

def draw_atom(image_size=(150, 150), proton_circle_color=(255, 0, 0, 255), 
              electron_color=(0, 0, 255, 255), protons=6, neutrons=6, electrons=6, 
              nucleus_radius=10, electron_radius=5, orbit_spacing=20, 
              electron_threshold=20, scale_factor=0.5, unstable_isotope=False, 
              radiation_type=None, logo_path=None, alpha_path=None, beta_path=None, gamma_path=None):
    
    # Create a new image with a transparent background
    img = Image.new('RGBA', image_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Calculate the position of the nucleus
    nucleus_position = (image_size[0] // 2, image_size[1] // 2)

    # Adjust size if the number of electrons exceeds the threshold
    if electrons > electron_threshold:
        nucleus_radius *= scale_factor
        electron_radius *= scale_factor
        orbit_spacing *= scale_factor

    # Draw the proton circle
    proton_radius = nucleus_radius  # Radius for proton circle
    draw.ellipse((nucleus_position[0] - proton_radius, nucleus_position[1] - proton_radius,
                   nucleus_position[0] + proton_radius, nucleus_position[1] + proton_radius), 
                   fill=proton_circle_color)  # Red circle for protons

    # Draw the proton, neutron, and electron text in the bottom corner
    proton_text = f"{protons}+"
    neutron_text = f"{neutrons}N"
    electron_text = f"{electrons}-"
    
    # Draw text directly onto the image
    draw.text((5, image_size[1] - 40), proton_text, fill=(255, 255, 255, 255))
    draw.text((5, image_size[1] - 25), electron_text, fill=(255, 255, 255, 255))  # Moved above neutron text
    draw.text((5, image_size[1] - 10), neutron_text, fill=(255, 255, 255, 255))

    # Draw orbits and electrons
    orbit_number = 0
    while electrons > 0:
        # Define the maximum electrons for the current shell using the formula 2n^2
        max_electrons_in_shell = 2 * (orbit_number + 1) ** 2
        
        # Determine how many electrons can fit in the current shell
        electrons_in_shell = min(electrons, max_electrons_in_shell)
        orbit_radius = proton_radius + orbit_spacing * (orbit_number + 1)
        
        # Draw the orbit
        draw.ellipse((nucleus_position[0] - orbit_radius, nucleus_position[1] - orbit_radius,
                       nucleus_position[0] + orbit_radius, nucleus_position[1] + orbit_radius), 
                       outline=(255, 255, 255, 100))  # Light white for orbits

        # Draw electrons on the orbit
        for j in range(electrons_in_shell):
            angle = 2 * math.pi * j / electrons_in_shell  # Spread electrons evenly
            electron_x = nucleus_position[0] + orbit_radius * math.cos(angle)
            electron_y = nucleus_position[1] + orbit_radius * math.sin(angle)
            draw.ellipse((electron_x - electron_radius, electron_y - electron_radius,
                           electron_x + electron_radius, electron_y + electron_radius), 
                           fill=electron_color)

        # Subtract the electrons placed in the current shell
        electrons -= electrons_in_shell
        orbit_number += 1  # Move to the next shell

    # Draw the unstable isotope logo and radiation type if applicable
    if unstable_isotope and logo_path:
        try:
            logo = Image.open(logo_path)  # Load the logo image
            logo_size = 20  # Desired size of the logo
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)  # Resize the logo to fit
            logo_position = (image_size[0] - logo_size - 5, image_size[1] - logo_size - 5)
            img.paste(logo, logo_position, logo)  # Paste the logo in the bottom right corner

            # Load the radiation type symbol image
            if radiation_type:
                radiation_image_map = {
                    "Alpha": alpha_path,
                    "Beta": beta_path,
                    "Gamma": gamma_path,
                }
                radiation_image_path = radiation_image_map.get(radiation_type)
                if radiation_image_path:
                    radiation_symbol = Image.open(radiation_image_path)
                    radiation_symbol_size = 15
                    radiation_symbol = radiation_symbol.resize((radiation_symbol_size, radiation_symbol_size),
                                                                Image.LANCZOS)
                    # Position the radiation symbol next to the logo
                    symbol_position = (logo_position[0] - radiation_symbol_size - 5, logo_position[1])
                    img.paste(radiation_symbol, symbol_position, radiation_symbol)
        except Exception as e:
            print(f"Error loading or pasting the logo/symbol: {e}")

    return img

# Command-line parameters
parser = argparse.ArgumentParser(description='Generate an atom image.')
parser.add_argument('protons', nargs='?', type=int, default=1)
parser.add_argument('neutrons', nargs='?', type=int, default=0)
parser.add_argument('electrons', nargs='?', type=int, default=1)
args = parser.parse_args()

# Customizable parameters
custom_image_size = (150, 150)
custom_proton_circle_color = (255, 0, 0, 255)  # Red for protons
custom_electron_color = (0, 0, 255, 255)  # Blue for electrons
custom_protons = args.protons
custom_neutrons = args.neutrons
custom_electrons = args.electrons
custom_nucleus_radius = 10
custom_electron_radius = 5
custom_orbit_spacing = 20
custom_electron_threshold = 20  # Threshold for scaling down
custom_scale_factor = 0.5  # Factor to scale down the atom size
custom_unstable_isotope = False  # Set to True to display the unstable isotope logo
custom_radiation_type = "beta"  # Type of radiation
custom_logo_path = r'\Unstable.png'
custom_alpha_path = r'alpha.png'
custom_beta_path = r'beta.png'
custom_gamma_path = r'gamma.png'

# Generate the atom image
atom_image = draw_atom(
    image_size=custom_image_size,
    proton_circle_color=custom_proton_circle_color,
    electron_color=custom_electron_color,
    protons=custom_protons,
    neutrons=custom_neutrons,
    electrons=custom_electrons,
    nucleus_radius=custom_nucleus_radius,
    electron_radius=custom_electron_radius,
    orbit_spacing=custom_orbit_spacing,
    electron_threshold=custom_electron_threshold,
    scale_factor=custom_scale_factor,
    unstable_isotope=custom_unstable_isotope,
    radiation_type=custom_radiation_type,
    logo_path=custom_logo_path,
    alpha_path=custom_alpha_path,
    beta_path=custom_beta_path,
    gamma_path=custom_gamma_path
)

# Save the image
output_path = Path(__file__).resolve().parent / 'atom.png'
atom_image.save(output_path)

# Display the image
atom_image.show()
