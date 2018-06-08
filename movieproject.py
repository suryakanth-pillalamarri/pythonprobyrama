
import media

import fresh_tomatos

bn=media.Movie("BHARATH ANE NANU",

                     'A STOREY OF A CHEIF MINISTER',

                     'index.jpeg',
                     'https://www.youtube.com/watch?v=KMWS5y2gZ6E')

Om_namo_venkatesaya=media.Movie("OM NAMO VENKATESAYA",

                     'A STOREY OF A DECIPLE',

                    'omnamovenkatesaya.jpeg' ,
                     'https://www.youtube.com/watch?v=Tcy4M7P2CRI&t=3s')

jai_lavakusa=media.Movie("JAI LAVA KUSA",

                         'GOOD RELATION BETWEEN BROTHERS',

                         'jai_lava_kusa_new_posters_and_photos_1309170321_04.jpg',

                         'https://www.youtube.com/watch?v=5N-wb-OGa1I')

mahabarath=media.Movie('MAHABARATH',

                       'STOREY OF LIFE',

                       'http://media2.intoday.in/indiatoday/images/stories/2013november/mahabharat_story-size_660_111913034235.jpg',

                       'https://www.youtube.com/watch?v=cSFW55HB-a8')

avathar2=media.Movie('AVATAR',

                     'STOREY OF A MAN',

                    'http://cdn.breathecast.com/data/images/full/25000/avatar-2-return-to-pandora-poster.jpg?w=600',

                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')
movies=[bn,Om_namo_venkatesaya,jai_lavakusa,mahabarath,avathar2]#war_with_planet_of_apes]

fresh_tomatos.open_movies_page(movies)


