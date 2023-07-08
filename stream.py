import streamlit as st
from lightgbm import LGBMClassifier
from joblib import load
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import random
from math import *
import time
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"gif"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('galaxy-knowledge1.gif')

model = load('lgbm.pkl')
sc=load('std_scaler.bin')

gas = ['Gas Giant.png', 'Gas Giant2.png']
ice = ['Neptune-like.png', 'Neptune-like2.png']
superEarth = ['Super Earth.png']
terrestrial = ['Terrestrial.png', 'Terrestrial2.png', 'Terrestrial3.png']

st.title("Exoplanet Simulator")
x = 10
if x == 10:
    with st.chat_message("user"):
        st.text("Move the sliders around to experiment and see what type of planet is formed.")
        st.write("Hint: Ice & Gas Giants lack solid surfaces as they lack heavy elements needed to form rocky planets during the early stages of a solar system. Terrestrial planets are smaller because there is less material available to form a solid surface due to an abundance of lighter elements like Hydrogen compared to heavier elements like Iron. Try Creating Terrestrial Planets by keeping the radius and mass below 2.")

x = st.slider("Planet Mass (w.t.r Earth)",min_value=0.09, max_value=49.9)
y = st.slider("Planet Radius (w.t.r Earth)",min_value=0.09, max_value=49.9)

if x > 0.09 and y > 0.09:
    st.header("Your planet is being created...")
    time.sleep(2)
    
    q = model.predict(sc.transform([[x,y]]))

    
    if (q == ['Super Earth']):
        st.image(superEarth[0])
        st.header("Planet created: Super Earth (Reference Image Above)")
        st.subheader("Description:")
        st.write("Super Earths are a class of exoplanets that are larger and more massive than Earth but smaller than gas giants. These rocky worlds, often referred to as super-sized versions of our planet, can vary in size and composition. They have solid surfaces and may possess atmospheres and water in different states. Super Earths offer intriguing possibilities for habitability and provide valuable insights into the diversity of planetary systems beyond our solar system.")
    if (q == ['Terrestrial']):
        st.image(terrestrial[random.randint(0,2)])
        st.header("Planet created: Terrestrial Planet (Reference Image Above)")
        st.subheader("Description:")
        st.write("Terrestrial planets, also known as rocky planets, are a class of planets that share similar characteristics to Earth. They are primarily composed of silicate rocks and metals, with a solid surface. Terrestrial planets are relatively smaller in size compared to gas giants and are typically found closer to their host star in planetary systems. They often possess thin atmospheres, if any, and may have features such as mountains, valleys, and even bodies of water. These planets are of particular interest in the search for extraterrestrial life, as they offer the potential for habitability and the presence of complex organic molecules.")
    if (q == ['Neptune-like']):
        st.image(ice[random.randint(0,1)])
        st.header("Planet created: Ice Giant (Reference Image Above)")
        st.subheader("Description:")
        st.write("Ice giants are planets larger than Earth but smaller than gas giants, composed of rock, metal, and a thick layer of icy materials. Their atmospheres contain hydrogen, helium, and ice, giving them a bluish hue. Ice giants, like Uranus and Neptune, display complex weather patterns and have moons with potential geologic activity. Studying ice giants enhances our understanding of planetary systems and the diverse compositions and atmospheres found in the universe.")
    if (q == ['Gas Giant']):
        st.image(gas[random.randint(0,1)])
        st.header("Planet created: Gas Giant (Reference Image Above)")
        st.subheader("Description:")
        st.write("Gas giants are enormous planets with extensive atmospheres primarily composed of hydrogen and helium. They lack a solid surface and have massive gravitational pulls. These giant planets exhibit dynamic weather patterns, including powerful storms. Gas giants often have rings and are accompanied by a system of moons. They play a crucial role in shaping planetary systems and provide insights into planetary formation and evolution.")

        
    with st.chat_message("assistant"):
        if (q == ['Super Earth']):
            succ = st.success("You have created a planet which may potentially be habitable!")
        if (q == ['Terrestrial']):
            succ = st.success("You have created a planet which may potentially be habitable!")
        if (q == ['Neptune-like']):
            warn = st.error("You have created a planet which cannot be habitable! Please create a new planet.")
        if (q == ['Gas Giant']):
            warn = st.error("You have created a planet which cannot be habitable! Please create a new planet.")

        st.divider()

    if (q == ['Super Earth']) or (q == ['Terrestrial']):

        st.text("Move the sliders around and experiment with them to create the star for your planet.")
        temp = st.slider("Surface Temperature of Star (in Kelvins)",min_value=3000, max_value=10000)
        radius = st.slider("Star Radius (w.t.r sun)",min_value=1, max_value=50)
        radius = radius*696340000
        st.write("Suggested Resource for Better Understanding:")
        st.video("luminosity.mp4")

    if temp > 3000 and radius > 1:

        if temp >= 10000 and temp < 30000:
            st.subheader("B type star (Image Below for Reference)")
            st.image('b_type.png')
            st.write("B-type stars are among the hottest and most luminous main-sequence stars. They have surface temperatures ranging from 10,000 to 30,000 Kelvin. These stars appear blue or bluish-white in color and emit a significant amount of ultraviolet radiation. B-type stars have strong absorption lines of neutral helium in their spectra. They are relatively rare compared to other types of stars.")
        elif temp >= 7500 and 10000 < 30000:
            st.subheader("A type star (Image Below for Reference)")
            st.image('a_type.png')
            st.write("A-type stars are also main-sequence stars, but slightly cooler than B-type stars. They have surface temperatures ranging from 7,500 to 10,000 Kelvin. A-type stars appear white or bluish-white in color. They have prominent hydrogen absorption lines in their spectra, as well as ionized metals. A-type stars are generally more common than B-type stars.")
        elif temp >= 6000 and temp < 7500:
            st.subheader("F type star (Image Below for Reference)")
            st.image('f_type.png')
            st.write("F-type stars are intermediate in temperature between A-type and G-type stars. They have surface temperatures ranging from 6,000 to 7,500 Kelvin. F-type stars appear yellowish-white in color and have weaker hydrogen absorption lines compared to A-type stars. They exhibit stronger ionized metal lines, particularly calcium. F-type stars, like our Sun, are common in the galaxy.")
        elif temp >= 5200 and temp < 6000:
            st.subheader("G type star (Image Below for Reference)")
            st.image('g_type.png')
            st.write("G-type stars, also known as yellow dwarfs, are similar to our Sun in terms of temperature and characteristics. They have surface temperatures ranging from 5,000 to 6,000 Kelvin. G-type stars appear yellow in color and have a well-defined spectrum with prominent hydrogen absorption lines. Our Sun is a G-type star, and these stars are considered to be in the middle of the temperature and luminosity range.")
        elif temp >= 3700 and temp < 5200:
            st.subheader("K type star (Image Below for Reference)")
            st.image('k_type.png')
            st.write("K-type stars are cooler than G-type stars and appear orange in color. They have surface temperatures ranging from 3,500 to 5,000 Kelvin. K-type stars have weaker hydrogen absorption lines and prominent lines of ionized metals such as calcium and sodium in their spectra. These stars are relatively common and include many red giants and orange dwarfs.")
        elif temp >= 2400 and temp < 3700:
            st.subheader("M type star (Image Below for Reference)")
            st.image('m_type.png')
            st.write("M-type stars, also known as red dwarfs, are the coolest and most common type of main-sequence stars in the galaxy. They have surface temperatures below 3,500 Kelvin. M-type stars appear red in color and have weak hydrogen absorption lines. Their spectra contain strong molecular absorption bands, particularly of molecules like titanium oxide and water vapor. M-type stars are known for their longevity and can live for tens of billions of years.")

        st.divider()

        if temp > 3000 and radius > 1:

            Luminosity = float(4* pi * (radius**2) * 5.670373 * 10**(-8) * (temp**4))
            Luminosity = round(Luminosity)
            st.write("The Luminosity of the Star is: " + str("{:,}".format(Luminosity)) + ' ' + 'watts')
            st.write("The luminosity of a star is the energy emitted over time. It remains constant if the star is stable and doesn't change over distances. The intensity of a star is the luminosity over a specific area. It varies depending on the distance from the star and can increase or decrease based on position, while the luminosity remains unchanged. The star's surface temperature and radius determine its luminosity, which helps identify its type, age, life, and behavior.")
            habitual1 = (142120000000 * sqrt(Luminosity/(3.827 * 10**26)))/(1.496 * 10**11)
            habitual10 = str(habitual1) + ' ' + 'AU'
            habitual2 = 204952000000 * sqrt(Luminosity/(3.827 * 10**26))/(1.496 * 10**11)
            habitual20 = str(habitual2) + ' ' + 'AU'

            st.divider()
            
            st.write("The Habitual zone is where liquid water can exist, allowing for the potential of organic life. It's an area with optimal conditions, neither too hot nor too cold. In our solar system, it spans from 0.95 AU to 1.37 AU from the sun. The existence of life in a planet depends on whether it falls within this zone, which is determined by the star's luminosity. Planets outside this range would not be suitable for supporting life. In this case the Habitual Zone would be:")
            st.write("Starting Point: -" + ' ' + str(habitual10) + ' ' + 'from the star')
            st.write("Ending Point: -" + ' ' + str(habitual20) + ' ' + 'from the star.')
            
            st.text("Drag the slider and try locating your planet under the habitable zone")

            st.write("The full form of AU is 'Astronomical Unit' which is the distance between Earth and the Sun. It is generally used to define distances along with light years in the universe. 1 AU is equivalent to 149,600,000 kilometers.")

            distance = st.slider("Distance from the star (in AU)",min_value=0.9, max_value=149.9)
            if distance > 0.9: 
                if distance > habitual1 and distance < habitual2:
                    st.success("Your planet falls under the habitable zone! It has the potential to support life!")
                else:
                    st.error("Your planet does not fall under the habitual zone! Please change its distance from the star so that it has the potential to support life!")

