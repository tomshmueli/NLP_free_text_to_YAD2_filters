from bs4 import BeautifulSoup

# Replace this with a representative portion of the actual HTML content you copied
html_content = """<div class="options-list_checkbox__10fMZ"><label data-testid="check-button"><input 
data-testid="image-checkbox" readonly="" tabindex="-1" type="checkbox" class="check-button_input__YX3KQ" 
value="193"><div class="image-checkbox_imageCheckbox___tM0b"><div><div class="image-checkbox_image__MPczk"><img 
alt="BAW" loading="lazy" decoding="async" data-nimg="fill" sizes="(max-width: 880px) 48px, 
28px" srcset="/vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2
&amp;w=16&amp;q=75 16w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png
%3Fver%3D2&amp;w=32&amp;q=75 32w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer
%2F193.png%3Fver%3D2&amp;w=48&amp;q=75 48w, 
/vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2&amp;w=64&amp
;q=75 64w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2
&amp;w=96&amp;q=75 96w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png
%3Fver%3D2&amp;w=128&amp;q=75 128w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles
%2Fmanufacturer%2F193.png%3Fver%3D2&amp;w=256&amp;q=75 256w, 
/vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2&amp;w=384&amp
;q=75 384w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2
&amp;w=640&amp;q=75 640w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193
.png%3Fver%3D2&amp;w=750&amp;q=75 750w, 
/vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2&amp;w=828&amp
;q=75 828w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2
&amp;w=1080&amp;q=75 1080w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193
.png%3Fver%3D2&amp;w=1200&amp;q=75 1200w, 
/vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2&amp;w=1920
&amp;q=75 1920w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver
%3D2&amp;w=2048&amp;q=75 2048w, /vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer
%2F193.png%3Fver%3D2&amp;w=3840&amp;q=75 3840w" 
src="/vehicles/_next/image?url=https%3A%2F%2Fassets.yad2.co.il%2Fvehicles%2Fmanufacturer%2F193.png%3Fver%3D2&amp;w
=3840&amp;q=75" style="position: absolute; height: 100%; width: 100%; inset: 0px; color: transparent;"></div><span 
class="image-checkbox_text___iiof"><span>BAW</span></span><svg width="1em" height="1em" viewBox="0 0 24 24" 
fill="none" xmlns="http://www.w3.org/2000/svg" class="image-checkbox_checkedIcon__H8zYo"><path d="M19.938 
5.492a.75.75 0 011.172.929l-.069.087L9.804 18.724a1.752 1.752 0 01-2.565.012l-.104-.122-4.727-6.068a.75.75 0 
011.11-1.004l.074.082 4.727 6.069a.25.25 0 00.35.043l.031-.028L19.938 5.492z" 
fill="currentColor"></path></svg></div></div></label></div>"""


def extract_manufacturers_mapping():
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    options = soup.find_all('div', class_='options-list_checkbox__10fMZ')
    # Extract the mappings
    manufacturer_mapping = {}
    for option in options:
        input_element = option.find('input')
        value = input_element['value']
        label_element = option.find('span', class_='image-checkbox_text___iiof')
        if label_element:
            label = label_element.text.strip()
            manufacturer_mapping[label] = value

    # Print the mappings
    print("Manufacturer Mapping:", manufacturer_mapping)
    return manufacturer_mapping
