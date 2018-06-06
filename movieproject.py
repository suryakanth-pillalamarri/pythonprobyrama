import media

import fresh_tomatos

bahubali=media.Movie("BAHUBALI",

                     'A STOREY OF A KING',

                     'https://sp.yimg.com/ib/th?id=OIP.HD1It_lzt0fdVmj5TbiRwwDKEs&pid=15.1&rs=1&c=1&qlt=95&w=81&h=120',

                     'https://www.youtube.com/watch?v=qD-6d8Wo3do')

Om_namo_venkatesaya=media.Movie("OM NAMO VENKATESAYA",

                     'A STOREY OF A DECIPLE',

                    'https://tse3.mm.bing.net/th?id=OIP.vMvqp_LDK0ON_jV7HtozWgD8D3&pid=15.1&P=0&w=172&h=170',

                     'https://www.youtube.com/watch?v=Tcy4M7P2CRI')

jai_lavakusa=media.Movie("JAI LAVA KUSA",

                         'GOOD RELATION BETWEEN BROTHERS',

                         'https://tse2.mm.bing.net/th?id=OIP.9uLooRFMAmfe-aC_cP1UdQE_DD&pid=15.1&P=0&w=321&h=197',

                         'https://www.youtube.com/watch?v=5N-wb-OGa1I')

mahabarath=media.Movie('MAHABARATH',

                       'STOREY OF LIFE',

                       'http://media2.intoday.in/indiatoday/images/stories/2013november/mahabharat_story-size_660_111913034235.jpg',

                       'https://www.youtube.com/watch?v=cSFW55HB-a8')

avathar2=media.Movie('AVATAR',

                     'STOREY OF A MAN',

                    'http://cdn.breathecast.com/data/images/full/25000/avatar-2-return-to-pandora-poster.jpg?w=600',

                     'https://www.youtube.com/watch?v=ZUgjaUZBP7o')



movies=[bahubali,Om_namo_venkatesaya,jai_lavakusa,mahabarath,avathar2]#war_with_planet_of_apes]

fresh_tomatos.open_movies_page(movies)
