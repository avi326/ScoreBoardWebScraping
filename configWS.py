COUNTRY_IDX = 1
URL_IDX = 0
LEAGUE_IDX = 2
URL = 'https://www.scoreboard.com/en/soccer/'
REQUIRED_NUM_OF_ARGS = 3
ARG_OPTION = 1
ARG_FILE_NAME = 2
PRINT = -1
DELAY = 2
'should add to .gitignore under *configWS.py'
links = ['https://www.scoreboard.com/en/soccer/bermuda/premier-league/', 'https://www.scoreboard.com/en/soccer/canada/canadian-premier-league/', 'https://www.scoreboard.com/en/soccer/costa-rica/primera-division/', 'https://www.scoreboard.com/en/soccer/dominican-republic/ldf/', 'https://www.scoreboard.com/en/soccer/el-salvador/primera-division/', 'https://www.scoreboard.com/en/soccer/guatemala/liga-nacional/', 'https://www.scoreboard.com/en/soccer/haiti/championnat-national/', 'https://www.scoreboard.com/en/soccer/honduras/liga-nacional/', 'https://www.scoreboard.com/en/soccer/jamaica/premier-league/', 'https://www.scoreboard.com/en/soccer/mexico/liga-mx/', 'https://www.scoreboard.com/en/soccer/nicaragua/liga-primera/', 'https://www.scoreboard.com/en/soccer/panama/lpf/', 'https://www.scoreboard.com/en/soccer/trinidad-and-tobago/pro-league/', 'https://www.scoreboard.com/en/soccer/usa/mls/', 'https://www.scoreboard.com/en/soccer/argentina/superliga/', 'https://www.scoreboard.com/en/soccer/aruba/division-di-honor/', 'https://www.scoreboard.com/en/soccer/bolivia/division-profesional/', 'https://www.scoreboard.com/en/soccer/brazil/serie-a/', 'https://www.scoreboard.com/en/soccer/chile/primera-division/', 'https://www.scoreboard.com/en/soccer/colombia/liga-aguila/', 'https://www.scoreboard.com/en/soccer/ecuador/liga-pro/', 'https://www.scoreboard.com/en/soccer/paraguay/primera-division/', 'https://www.scoreboard.com/en/soccer/peru/liga-1/', 'https://www.scoreboard.com/en/soccer/uruguay/primera-division/', 'https://www.scoreboard.com/en/soccer/venezuela/primera-division/', 'https://www.scoreboard.com/en/soccer/albania/superliga/', 'https://www.scoreboard.com/en/soccer/andorra/primera-divisio/', 'https://www.scoreboard.com/en/soccer/armenia/premier-league/', 'https://www.scoreboard.com/en/soccer/austria/tipico-bundesliga/', 'https://www.scoreboard.com/en/soccer/azerbaijan/premier-league/', 'https://www.scoreboard.com/en/soccer/belarus/vysshaya-liga/', 'https://www.scoreboard.com/en/soccer/belgium/jupiler-league/', 'https://www.scoreboard.com/en/soccer/bosnia-and-herzegovina/premier-league/', 'https://www.scoreboard.com/en/soccer/bulgaria/parva-liga/', 'https://www.scoreboard.com/en/soccer/croatia/1-hnl/', 'https://www.scoreboard.com/en/soccer/cyprus/first-division/', 'https://www.scoreboard.com/en/soccer/czech-republic/1-liga/', 'https://www.scoreboard.com/en/soccer/denmark/superliga/', 'https://www.scoreboard.com/en/soccer/england/premier-league/', 'https://www.scoreboard.com/en/soccer/estonia/meistriliiga/', 'https://www.scoreboard.com/en/soccer/faroe-islands/premier-league/', 'https://www.scoreboard.com/en/soccer/finland/veikkausliiga/', 'https://www.scoreboard.com/en/soccer/france/ligue-1/', 'https://www.scoreboard.com/en/soccer/georgia/crystalbet-erovnuli-liga/', 'https://www.scoreboard.com/en/soccer/germany/bundesliga/', 'https://www.scoreboard.com/en/soccer/gibraltar/gibraltar-cup/', 'https://www.scoreboard.com/en/soccer/greece/super-league/', 'https://www.scoreboard.com/en/soccer/hungary/otp-bank-liga/', 'https://www.scoreboard.com/en/soccer/iceland/pepsideild/', 'https://www.scoreboard.com/en/soccer/ireland/premier-division/', 'https://www.scoreboard.com/en/soccer/israel/ligat-ha-al/', 'https://www.scoreboard.com/en/soccer/italy/serie-a/', 'https://www.scoreboard.com/en/soccer/kazakhstan/premier-league/', 'https://www.scoreboard.com/en/soccer/kosovo/superliga/', 'https://www.scoreboard.com/en/soccer/latvia/optibet-virsliga/', 'https://www.scoreboard.com/en/soccer/liechtenstein/liechtenstein-cup/', 'https://www.scoreboard.com/en/soccer/lithuania/a-lyga/', 'https://www.scoreboard.com/en/soccer/luxembourg/national-division/', 'https://www.scoreboard.com/en/soccer/malta/premier-league/', 'https://www.scoreboard.com/en/soccer/moldova/divizia-nationala/', 'https://www.scoreboard.com/en/soccer/montenegro/prva-crnogorska-liga/', 'https://www.scoreboard.com/en/soccer/netherlands/eredivisie/', 'https://www.scoreboard.com/en/soccer/northern-ireland/nifl-premiership/', 'https://www.scoreboard.com/en/soccer/north-macedonia/1-mfl/', 'https://www.scoreboard.com/en/soccer/norway/eliteserien/', 'https://www.scoreboard.com/en/soccer/poland/ekstraklasa/', 'https://www.scoreboard.com/en/soccer/portugal/primeira-liga/', 'https://www.scoreboard.com/en/soccer/romania/liga-1/', 'https://www.scoreboard.com/en/soccer/russia/premier-league/', 'https://www.scoreboard.com/en/soccer/san-marino/campionato-sammarinese/', 'https://www.scoreboard.com/en/soccer/scotland/premiership/', 'https://www.scoreboard.com/en/soccer/serbia/super-liga/', 'https://www.scoreboard.com/en/soccer/slovakia/fortuna-liga/', 'https://www.scoreboard.com/en/soccer/slovenia/prva-liga/', 'https://www.scoreboard.com/en/soccer/spain/laliga/', 'https://www.scoreboard.com/en/soccer/sweden/allsvenskan/', 'https://www.scoreboard.com/en/soccer/switzerland/super-league/', 'https://www.scoreboard.com/en/soccer/turkey/super-lig/', 'https://www.scoreboard.com/en/soccer/ukraine/premier-league/', 'https://www.scoreboard.com/en/soccer/wales/cymru-premier/', 'https://www.scoreboard.com/en/soccer/bahrain/premier-league/', 'https://www.scoreboard.com/en/soccer/bangladesh/premier-league/', 'https://www.scoreboard.com/en/soccer/cambodia/c-league/', 'https://www.scoreboard.com/en/soccer/china/super-league/', 'https://www.scoreboard.com/en/soccer/hong-kong/premier-league/', 'https://www.scoreboard.com/en/soccer/india/isl/', 'https://www.scoreboard.com/en/soccer/indonesia/liga-1/', 'https://www.scoreboard.com/en/soccer/iran/persian-gulf-pro-league/', 'https://www.scoreboard.com/en/soccer/iraq/super-league/', 'https://www.scoreboard.com/en/soccer/japan/j1-league/', 'https://www.scoreboard.com/en/soccer/jordan/premier-league/', 'https://www.scoreboard.com/en/soccer/kuwait/premier-league/', 'https://www.scoreboard.com/en/soccer/kyrgyzstan/premier-liga/', 'https://www.scoreboard.com/en/soccer/lebanon/premier-league/', 'https://www.scoreboard.com/en/soccer/macao/elite-league/', 'https://www.scoreboard.com/en/soccer/malaysia/super-league/', 'https://www.scoreboard.com/en/soccer/maldives/dhivehi-premier-league/', 'https://www.scoreboard.com/en/soccer/myanmar/national-league/', 'https://www.scoreboard.com/en/soccer/oman/professional-league/', 'https://www.scoreboard.com/en/soccer/pakistan/premier-league/', 'https://www.scoreboard.com/en/soccer/palestine/west-bank-league/', 'https://www.scoreboard.com/en/soccer/philippines/pfl/', 'https://www.scoreboard.com/en/soccer/qatar/qsl/', 'https://www.scoreboard.com/en/soccer/saudi-arabia/saudi-professional-league/', 'https://www.scoreboard.com/en/soccer/singapore/premier-league/', 'https://www.scoreboard.com/en/soccer/south-korea/k-league-1/', 'https://www.scoreboard.com/en/soccer/sri-lanka/champions-league/', 'https://www.scoreboard.com/en/soccer/syria/premier-league/', 'https://www.scoreboard.com/en/soccer/taiwan/premier-league/', 'https://www.scoreboard.com/en/soccer/tajikistan/vysshaya-liga/', 'https://www.scoreboard.com/en/soccer/thailand/thai-league-1/', 'https://www.scoreboard.com/en/soccer/turkmenistan/yokary-liga/', 'https://www.scoreboard.com/en/soccer/united-arab-emirates/uae-league/', 'https://www.scoreboard.com/en/soccer/uzbekistan/super-league/', 'https://www.scoreboard.com/en/soccer/vietnam/v-league-1/', 'https://www.scoreboard.com/en/soccer/yemen/division-1/', 'https://www.scoreboard.com/en/soccer/australia/a-league/', 'https://www.scoreboard.com/en/soccer/new-zealand/football-championship/', 'https://www.scoreboard.com/en/soccer/algeria/ligue-1/', 'https://www.scoreboard.com/en/soccer/angola/girabola/', 'https://www.scoreboard.com/en/soccer/benin/ligue-1/', 'https://www.scoreboard.com/en/soccer/botswana/premier-league/', 'https://www.scoreboard.com/en/soccer/burkina-faso/premier-league/', 'https://www.scoreboard.com/en/soccer/burundi/primus-league/', 'https://www.scoreboard.com/en/soccer/cameroon/elite-one/', 'https://www.scoreboard.com/en/soccer/cape-verde/campeonato-nacional/', 'https://www.scoreboard.com/en/soccer/djibouti/division-1/', 'https://www.scoreboard.com/en/soccer/dr-congo/ligue-1/', 'https://www.scoreboard.com/en/soccer/egypt/premier-league/', 'https://www.scoreboard.com/en/soccer/eswatini/swazi-mtn-premier-league/', 'https://www.scoreboard.com/en/soccer/ethiopia/premier-league/', 'https://www.scoreboard.com/en/soccer/gabon/championnat-d1/', 'https://www.scoreboard.com/en/soccer/gambia/gfa-league/', 'https://www.scoreboard.com/en/soccer/ghana/premier-league/', 'https://www.scoreboard.com/en/soccer/guinea/ligue-1/', 'https://www.scoreboard.com/en/soccer/ivory-coast/ligue-1/', 'https://www.scoreboard.com/en/soccer/kenya/premier-league/', 'https://www.scoreboard.com/en/soccer/lesotho/premier-league/', 'https://www.scoreboard.com/en/soccer/liberia/lfa-first-division/', 'https://www.scoreboard.com/en/soccer/libya/premier-league/', 'https://www.scoreboard.com/en/soccer/malawi/super-league/', 'https://www.scoreboard.com/en/soccer/mali/premiere-division/', 'https://www.scoreboard.com/en/soccer/mauritania/ligue-1/', 'https://www.scoreboard.com/en/soccer/mauritius/mauritian-league/', 'https://www.scoreboard.com/en/soccer/morocco/botola-pro/', 'https://www.scoreboard.com/en/soccer/mozambique/mocambola/', 'https://www.scoreboard.com/en/soccer/namibia/mtc-premiership/', 'https://www.scoreboard.com/en/soccer/niger/ligue-1/', 'https://www.scoreboard.com/en/soccer/nigeria/npfl/', 'https://www.scoreboard.com/en/soccer/republic-of-the-congo/ligue-1/', 'https://www.scoreboard.com/en/soccer/reunion/regionale-1/', 'https://www.scoreboard.com/en/soccer/rwanda/national-football-league/', 'https://www.scoreboard.com/en/soccer/senegal/ligue-1/', 'https://www.scoreboard.com/en/soccer/seychelles/first-division-league/', 'https://www.scoreboard.com/en/soccer/sierra-leone/premier-league/', 'https://www.scoreboard.com/en/soccer/somalia/nation-link-telecom-championship/', 'https://www.scoreboard.com/en/soccer/south-africa/premier-league/', 'https://www.scoreboard.com/en/soccer/sudan/premier-league/', 'https://www.scoreboard.com/en/soccer/tanzania/ligi-kuu-bara/', 'https://www.scoreboard.com/en/soccer/togo/championnat-national/', 'https://www.scoreboard.com/en/soccer/tunisia/ligue-professionnelle-1/', 'https://www.scoreboard.com/en/soccer/uganda/premier-league/', 'https://www.scoreboard.com/en/soccer/zambia/super-league/']