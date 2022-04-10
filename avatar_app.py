#!/usr/bin/python3

import streamlit as st
import py_avataaars as pav
from PIL import Image
import base64
from random import randrange


# Display avatar img in .svg
def render_svg(svg):
	b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
	html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
	st.write(html, unsafe_allow_html=True)

def main():
	st.set_page_config(layout="wide")
	st.title('Hello There... I am Shyamal.')
	st.header('This is The Avatar Generator')
	st.markdown(""" 
	> Here you can create you own custome avatars.

	> Click the arrow in top left for more options. 
	""")

	avt_style = st.selectbox('Background', ('CIRCLE', 'TRANSPARENT')) 


	# ************** List of avatar features ***************
	avt_skin_color = ['TANNED','YELLOW','PALE','LIGHT','BROWN','DARK_BROWN','BLACK']
	avt_top_type = ['NO_HAIR','EYE_PATCH','HAT','HIJAB','TURBAN',
	                 'WINTER_HAT1','WINTER_HAT2','WINTER_HAT3',
	                 'WINTER_HAT4','LONG_HAIR_BIG_HAIR','LONG_HAIR_BOB',
	                 'LONG_HAIR_BUN','LONG_HAIR_CURLY','LONG_HAIR_CURVY',
	                 'LONG_HAIR_DREADS','LONG_HAIR_FRIDA','LONG_HAIR_FRO',
	                 'LONG_HAIR_FRO_BAND','LONG_HAIR_NOT_TOO_LONG',
	                 'LONG_HAIR_SHAVED_SIDES','LONG_HAIR_MIA_WALLACE',
	                 'LONG_HAIR_STRAIGHT','LONG_HAIR_STRAIGHT2',
	                 'LONG_HAIR_STRAIGHT_STRAND','SHORT_HAIR_DREADS_01',
	                 'SHORT_HAIR_DREADS_02','SHORT_HAIR_FRIZZLE',
	                 'SHORT_HAIR_SHAGGY_MULLET','SHORT_HAIR_SHORT_CURLY',
	                 'SHORT_HAIR_SHORT_FLAT','SHORT_HAIR_SHORT_ROUND',
	                 'SHORT_HAIR_SHORT_WAVED','SHORT_HAIR_SIDES',
	                 'SHORT_HAIR_THE_CAESAR','SHORT_HAIR_THE_CAESAR_SIDE_PART']
	avt_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN',
	                   'BROWN_DARK','PASTEL_PINK','PLATINUM','RED','SILVER_GRAY']
	avt_hat_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02',
	                  'HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE',
	                  'PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']

	avt_facial_hair_type = ['DEFAULT','BEARD_MEDIUM','BEARD_LIGHT','BEARD_MAJESTIC','MOUSTACHE_FANCY','MOUSTACHE_MAGNUM']
	avt_facial_hair_color = ['AUBURN','BLACK','BLONDE','BLONDE_GOLDEN','BROWN','BROWN_DARK','PLATINUM','RED']
	avt_mouth_type = ['DEFAULT','CONCERNED','DISBELIEF','EATING','GRIMACE','SAD','SCREAM_OPEN','SERIOUS','SMILE','TONGUE','TWINKLE','VOMIT']
	avt_eye_type = ['DEFAULT','CLOSE','CRY','DIZZY','EYE_ROLL','HAPPY','HEARTS','SIDE','SQUINT','SURPRISED','WINK','WINK_WACKY']
	avt_eyebrow_type = ['DEFAULT','DEFAULT_NATURAL','ANGRY','ANGRY_NATURAL','FLAT_NATURAL','RAISED_EXCITED','RAISED_EXCITED_NATURAL','SAD_CONCERNED','SAD_CONCERNED_NATURAL','UNI_BROW_NATURAL','UP_DOWN','UP_DOWN_NATURAL','FROWN_NATURAL']
	avt_accessories_type = ['DEFAULT','KURT','PRESCRIPTION_01','PRESCRIPTION_02','ROUND','SUNGLASSES','WAYFARERS']
	avt_clothe_type = ['BLAZER_SHIRT','BLAZER_SWEATER','COLLAR_SWEATER','GRAPHIC_SHIRT','HOODIE','OVERALL','SHIRT_CREW_NECK','SHIRT_SCOOP_NECK','SHIRT_V_NECK']
	avt_clothe_color = ['BLACK','BLUE_01','BLUE_02','BLUE_03','GRAY_01','GRAY_02','HEATHER','PASTEL_BLUE','PASTEL_GREEN','PASTEL_ORANGE','PASTEL_RED','PASTEL_YELLOW','PINK','RED','WHITE']
	avt_clothe_graphic_type = ['BAT','CUMBIA','DEER','DIAMOND','HOLA','PIZZA','RESIST','SELENA','BEAR','SKULL_OUTLINE','SKULL']


	# ******** Random avatar features ************
	if st.button('Randomized Avatar'):
	    index_skin_color = randrange(0, len(avt_skin_color) )
	    index_top_type = randrange(0, len(avt_top_type) )
	    index_hair_color = randrange(0, len(avt_hair_color) )
	    index_hat_color = randrange(0, len(avt_hat_color) )
	    index_facial_hair_type = randrange(0, len(avt_facial_hair_type) )
	    index_facial_hair_color= randrange(0, len(avt_facial_hair_color) )
	    index_mouth_type = randrange(0, len(avt_mouth_type) )
	    index_eye_type = randrange(0, len(avt_eye_type) )
	    index_eyebrow_type = randrange(0, len(avt_eyebrow_type) )
	    index_accessories_type = randrange(0, len(avt_accessories_type) )
	    index_clothe_type = randrange(0, len(avt_clothe_type) )
	    index_clothe_color = randrange(0, len(avt_clothe_color) )
	    index_clothe_graphic_type = randrange(0, len(avt_clothe_graphic_type) )

	# ******** Default avatar features ************
	else:
	    index_skin_color = 0
	    index_top_type = 0
	    index_hair_color = 0
	    index_hat_color = 0
	    index_facial_hair_type = 0
	    index_facial_hair_color = 0
	    index_mouth_type = 0
	    index_eye_type = 0
	    index_eyebrow_type = 0
	    index_accessories_type = 0
	    index_clothe_type = 0
	    index_clothe_color = 0
	    index_clothe_graphic_type = 0

	option_skin_color = st.sidebar.selectbox('Skin color',avt_skin_color,index=index_skin_color)


	# ************** Avatar Head Features *************
	st.sidebar.subheader('Head top')

	option_top_type = st.sidebar.selectbox('Head top',avt_top_type, index = index_top_type)
	option_hair_color = st.sidebar.selectbox('Hair color',avt_hair_color,index=index_hair_color)
	option_hat_color = st.sidebar.selectbox('Hat color',avt_hat_color,index = index_hat_color)


	# ************** Avatar Face Features *************
	st.sidebar.subheader('Face')

	option_facial_hair_type = st.sidebar.selectbox('Facial hair type',
													avt_facial_hair_type,
													index=index_facial_hair_type)

	option_facial_hair_color = st.sidebar.selectbox('Facial hair color',
	                                                avt_facial_hair_color,
	                                                index = index_facial_hair_color)

	option_mouth_type = st.sidebar.selectbox('Mouth type',
	                                          avt_mouth_type,
	                                          index = index_mouth_type)

	option_eye_type = st.sidebar.selectbox('Eye type',
	                                        avt_eye_type,
	                                        index = index_eye_type)

	option_eyebrow_type = st.sidebar.selectbox('Eyebrow type',
	                                            avt_eyebrow_type,
	                                            index = index_eyebrow_type)



	# ************** Avatar Clothes and accessories *************
	st.sidebar.subheader('Clothe and accessories')
	option_accessories_type = st.sidebar.selectbox('Accessories type',
	                                                avt_accessories_type,
	                                                index = index_accessories_type)

	option_clothe_type = st.sidebar.selectbox('Clothe type',
	                                           avt_clothe_type,
	                                           index = index_clothe_type)

	option_clothe_color = st.sidebar.selectbox('Clothe Color',
	                                            avt_clothe_color,
	                                            index = index_clothe_color)

	option_clothe_graphic_type = st.sidebar.selectbox('Clothe graphic type',
	                                                   avt_clothe_graphic_type,
	                                                   index = index_clothe_graphic_type)

	# Avatar Creation
	avatar = pav.PyAvataaar(
		style=eval('pav.AvatarStyle.%s' % avt_style),
	    skin_color=eval('pav.SkinColor.%s' % option_skin_color),
	    top_type=eval('pav.TopType.SHORT_HAIR_SHORT_FLAT.%s' % option_top_type),
	    hair_color=eval('pav.HairColor.%s' % option_hair_color),
	    hat_color=eval('pav.Color.%s' % option_hat_color),
	    facial_hair_type=eval('pav.FacialHairType.%s' % option_facial_hair_type),
	    facial_hair_color=eval('pav.HairColor.%s' % option_facial_hair_color),
	    mouth_type=eval('pav.MouthType.%s' % option_mouth_type),
	    eye_type=eval('pav.EyesType.%s' % option_eye_type),
	    eyebrow_type=eval('pav.EyebrowType.%s' % option_eyebrow_type),
	    nose_type=pav.NoseType.DEFAULT,
	    accessories_type=eval('pav.AccessoriesType.%s' % option_accessories_type),
	    clothe_type=eval('pav.ClotheType.%s' % option_clothe_type),
	    clothe_color=eval('pav.Color.%s' % option_clothe_color),
	    clothe_graphic_type=eval('pav.ClotheGraphicType.%s' %option_clothe_graphic_type)
	)


	col1, col2 = st.columns(2)

	# For Svg
	with col1:
		st.subheader("Rendered in .svg")
		avasvg = avatar.render_svg_file('avatar.svg')
		render_svg(avatar.render_svg())

	# For Png
	with col2:
		st.subheader("Rendered in .png")
		avapng = avatar.render_png_file('avatar.png')
		image = Image.open('avatar.png')
		st.image(image)

if __name__ == "__main__":

	main()