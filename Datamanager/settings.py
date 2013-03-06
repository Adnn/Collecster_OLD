SCALE_FACTOR = 4 

# (510, 210) is a 1.7" * 0.7" tag, at 300dpi
TAG_WIDTH = 510 * SCALE_FACTOR
TAG_HEIGHT = 210 * SCALE_FACTOR

# A 0|1 boolean
TAG_BORDER = 1
#TAG_HEIGHT being reserved for the QR
TAG_LEFTCOLUMN_WIDTH = TAG_WIDTH-TAG_HEIGHT - 2*TAG_BORDER

TAG_ID_LEFTPADDING_CHARS = 5 
TAG_MAX_LINES = 3 
TAG_MAXLINES_COMPLEMENT = 2
TAG_MIN_COLS = 10 
TAG_MINCOLS_COMPLEMENT = 15 

TAG_FONT_TITLE = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'
TAG_FONT_DETAIL = '/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf'
TAG_FONT_CHECKSIGN = '/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf'

TAG_SUPERSAMPLE_FACTOR = 8
#The QR has to fit in the rightmost square of the tag (of side 210-border)
#all our QR will probably be ver1 (21x21), so : 21+(2*2) * 8 = 200
TAG_QR_BORDER = 2 
TAG_QR_BOXSIZE = 8 * SCALE_FACTOR

TAG_TEXT_BORDER_PAD = 6 * SCALE_FACTOR
TAG_INSTANCEDATA_SPACING = 15 * SCALE_FACTOR
TAG_INSTANCEDETAIL_HEIGHT = 75 * SCALE_FACTOR
#TAG_FONT_TITLESIZE = 12 * SCALE_FACTOR
TAG_FONT_DETAILSIZE = 33 * SCALE_FACTOR
TAG_FONT_CHECKSIGNSIZE = 40 * SCALE_FACTOR
TAG_CHECKBOX_SIDE = 30 * SCALE_FACTOR
TAG_CHECKSIGN_PAD = (3*SCALE_FACTOR, -6*SCALE_FACTOR)

PATH_MEDIA_INSTANCES = 'images/instances/'
PATH_TAGDIR = 'tag/'
PATH_TAGFILEFORMATSTRING = 'tag_%s.png'

URL_DM = 'dm/'
URL_ADD_INSTANCE = 'instance/add/'
URL_PRINT_INSTANCE = 'instance/print/'
URL_TAG_REDIRECT = 'admin/Datamanager/release/'

STR_WORK = u'Wk'
STR_LOOSE = u'l0'
