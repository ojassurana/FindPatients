import json
import requests
import pymongo
import difflib
import dns
global cities
global Status_Collection
global Information_Collection

client = pymongo.MongoClient("mongodb+srv://ojas:Ojulala02@cluster0.kfpcm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
cities = ['Achalpur', 'Achhnera', 'Adalaj', 'Adilabad', 'Adityapur', 'Adoni', 'Adoor', 'Adyar', 'Adra', 'Afzalpur',
          'Agartala', 'Agra', 'Ahmedabad', 'Ahmednagar', 'Aizawl', 'Ajmer', 'Akola', 'Akot', 'Alappuzha', 'Aligarh',
          'Alipurduar', 'Alirajpur', 'Allahabad', 'Alwar', 'Amalapuram', 'Amalner', 'Ambejogai', 'Ambikapur',
          'Amravati', 'Amreli', 'Amritsar', 'Amroha', 'Anakapalle', 'Anand', 'Anantapur', 'Anantnag', 'Anjar',
          'Anjangaon', 'Ankleshwar', 'Arakkonam', 'Araria', 'Arambagh', 'Arsikere', 'Arrah', 'Aruppukkottai', 'Arvi',
          'Arwal', 'Asansol', 'Asarganj', 'Ashok Nagar', 'Athni', 'Attingal', 'Aurangabad', 'Aurangabad', 'Azamgarh',
          'Bikaner', 'Bhiwandi', 'Bagaha', 'Bageshwar', 'Bahadurgarh', 'Baharampur', 'Bahraich', 'Balaghat', 'Balangir',
          'Baleshwar Town', 'Bengaluru', 'Bankura', 'Bapatla', 'Baramula', 'Barbil', 'Bargarh', 'Barh', 'Baripada Town',
          'Barnala', 'Barpeta', 'Batala', 'Bathinda', 'Begusarai', 'Belagavi', 'Bellampalle', 'Ballari', 'Belonia',
          'Bettiah', 'Bhabua', 'Bhadrachalam', 'Bhadrak', 'Bhagalpur', 'Bhainsa', 'Bharuch', 'Bhatapara', 'Bhavnagar',
          'Bhawanipatna', 'Bheemunipatnam', 'Bhilai Nagar', 'Bhilwara', 'Bhimavaram', 'Bhiwani', 'Bhongir', 'Bhopal',
          'Bhubaneswar', 'Bhuj', 'Bilaspur', 'Bobbili', 'Bodhan', 'Bokaro Steel City', 'Bongaigaon City', 'Brahmapur',
          'Buxar', 'Byasanagar', 'Chandausi', 'Chaibasa', 'Chandigarh', 'Charkhi Dadri', 'Chatra', 'Chalakudy',
          'Changanassery', 'Chennai', 'Cherthala', 'Chikkamagaluru', 'Chhapra', 'Chilakaluripet', 'Chirala',
          'Chirkunda', 'Chirmiri', 'Chittur-Thathamangalam', 'Chittoor', 'Coimbatore', 'Cuttack', 'Dalli-Rajhara',
          'Medininagar (Daltonganj)', 'Darbhanga', 'Darjiling', 'Davanagere', 'Deesa', 'Dehradun', 'Dehri-on-Sone',
          'Delhi', 'Deoghar', 'Dhamtari', 'Dhanbad', 'Dharmanagar', 'Dharmavaram', 'Dhenkanal', 'Dhoraji', 'Dhubri',
          'Dhule', 'Dhuri', 'Dibrugarh', 'Dimapur', 'Diphu', 'Kalyan-Dombivali', 'Dumka', 'Dumraon', 'Durg', 'Eluru',
          'Erode', 'English Bazar', 'Etawah', 'Faridabad', 'Faridkot', 'Firozabad', 'Farooqnagar', 'Fatehabad',
          'Fazilka', 'Forbesganj', 'Firozpur', 'Firozpur Cantt.', 'Fatehpur Sikri', 'Gadwal', 'Ganjbasoda', 'Gaya',
          'Giridih', 'Goalpara', 'Gobichettipalayam', 'Gobindgarh', 'Godhra', 'Gohana', 'Gokak', 'Gooty', 'Gopalganj',
          'Gudivada', 'Gudur', 'Gumia', 'Guntakal', 'Guntur', 'Gurdaspur', 'Gurgaon', 'Guruvayoor', 'Guwahati',
          'Gwalior', 'Habra', 'Hajipur', 'Haldwani', 'Hansi', 'Hapur', 'Hardwar', 'Hazaribag', 'Hindupur', 'Hisar',
          'Hoshiarpur', 'Hubli-Dharwad', 'Hugli-Chinsurah', 'Hyderabad', 'Ichalkaranji', 'Imphal', 'Indore', 'Itarsi',
          'Jabalpur', 'Jagdalpur', 'Jaggaiahpet', 'Jagraon', 'Jagtial', 'Jaipur', 'Jalandhar Cantt.', 'Jalandhar',
          'Jalpaiguri', 'Jamalpur', 'Jammalamadugu', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jamui', 'Jangaon', 'Jatani',
          'Jehanabad', 'Jhansi', 'Jhargram', 'Jharsuguda', 'Jhumri Tilaiya', 'Jind', 'Jorhat', 'Jodhpur', 'Kadapa',
          'Kadi', 'Kadiri', 'Kagaznagar', 'Kailasahar', 'Kaithal', 'Kakinada', 'Kalpi', 'Kalyan-Dombivali', 'Kamareddy',
          'Kancheepuram', 'Kandukur', 'Kanhangad', 'Kannur', 'Kanpur', 'Kapadvanj', 'Kapurthala', 'Karaikal',
          'Karimganj', 'Karimnagar', 'Karjat', 'Karnal', 'Karur', 'Karwar', 'Kasaragod', 'Kashipur', 'Kathua',
          'Katihar', 'Kavali', 'Kayamkulam', 'Kendrapara', 'Kendujhar', 'Keshod', 'Khair', 'Khambhat', 'Khammam',
          'Khanna', 'Kharagpur', 'Kharar', 'Khowai', 'Kishanganj', 'Kochi', 'Kodungallur', 'Kohima', 'Kolar', 'Kolkata',
          'Kollam', 'Korba', 'Koratla', 'Kot Kapura', 'Kothagudem', 'Kottayam', 'Kovvur', 'Kozhikode', 'Kunnamkulam',
          'Kurnool', 'Kyathampalle', 'Lachhmangarh', 'Ladnu', 'Ladwa', 'Lahar', 'Laharpur', 'Lakheri', 'Lakhimpur',
          'Lakhisarai', 'Lakshmeshwar', 'Lal Gopalganj Nindaura', 'Lalganj', 'Lalgudi', 'Lalitpur', 'Lalganj', 'Lalsot',
          'Lanka', 'Lar', 'Lathi', 'Latur', 'Lilong', 'Limbdi', 'Lingsugur', 'Loha', 'Lohardaga', 'Lonar', 'Lonavla',
          'Longowal', 'Loni', 'Losal', 'Lucknow', 'Ludhiana', 'Lumding', 'Lunawada', 'Lunglei', 'Macherla',
          'Machilipatnam', 'Madanapalle', 'Maddur', 'Madhepura', 'Madhubani', 'Madhugiri', 'Madhupur', 'Madikeri',
          'Madurai', 'Magadi', 'Mahad', 'Mahbubnagar', 'Mahalingapura', 'Maharajganj', 'Maharajpur', 'Mahasamund',
          'Mahe', 'Manendragarh', 'Mahendragarh', 'Mahesana', 'Mahidpur', 'Mahnar Bazar', 'Mahuva', 'Maihar',
          'Mainaguri', 'Makhdumpur', 'Makrana', 'Malda', 'Malaj Khand', 'Malappuram', 'Malavalli', 'Malegaon',
          'Malerkotla', 'Malkangiri', 'Malkapur', 'Malout', 'Malpura', 'Malur', 'Manachanallur', 'Manasa', 'Manavadar',
          'Manawar', 'Mancherial', 'Mandalgarh', 'Mandamarri', 'Mandapeta', 'Mandawa', 'Mandi', 'Mandi Dabwali',
          'Mandideep', 'Mandla', 'Mandsaur', 'Mandvi', 'Mandya', 'Maner', 'Mangaldoi', 'Mangaluru', 'Mangalvedhe',
          'Manglaur', 'Mangrol', 'Mangrol', 'Mangrulpir', 'Manihari', 'Manjlegaon', 'Mankachar', 'Manmad', 'Mansa',
          'Mansa', 'Manuguru', 'Manvi', 'Manwath', 'Mapusa', 'Margao', 'Margherita', 'Marhaura', 'Mariani', 'Marigaon',
          'Markapur', 'Marmagao', 'Masaurhi', 'Mathabhanga', 'Mattannur', 'Mathura', 'Mauganj', 'Mavelikkara', 'Mavoor',
          'Mayang Imphal', 'Medak', 'Medinipur', 'Meerut', 'Mehkar', 'Mahemdabad', 'Memari', 'Merta City', 'Mhaswad',
          'Mhow Cantonment', 'Mhowgaon', 'Mihijam', 'Mira-Bhayandar', 'Mirganj', 'Miryalaguda', 'Modasa', 'Modinagar',
          'Moga', 'Mohali', 'Mokameh', 'Mokokchung', 'Monoharpur', 'Moradabad', 'Morena', 'Morinda', 'Morshi', 'Morvi',
          'Motihari', 'Motipur', 'Mount Abu', 'Mudalagi', 'Mudabidri', 'Muddebihal', 'Mudhol', 'Mukerian', 'Mukhed',
          'Muktsar', 'Mul', 'Mulbagal', 'Multai', 'Greater Mumbai*', 'Mundi', 'Mundargi', 'Mungeli', 'Munger',
          'Murliganj', 'Murshidabad', 'Murtijapur', 'Murwara', 'Musabani', 'Mussoorie', 'Muvattupuzha', 'Muzaffarpur',
          'Nabadwip', 'Nabarangapur', 'Nabha', 'Nadbai', 'Nadiad', 'Nagaon', 'Nagapattinam', 'Nagar', 'Nagari',
          'Nagarkurnool', 'Nagaur', 'Nagda', 'Nagercoil', 'Nagina', 'Nagla', 'Nagpur', 'Nahan', 'Naharlagun',
          'Naidupet', 'Naihati', 'Naila Janjgir', 'Nainital', 'Nainpur', 'Najibabad', 'Nakodar', 'Nakur', 'Nalbari',
          'Namagiripettai', 'Namakkal', 'Nanded-Waghala', 'Nandgaon', 'Nandivaram-Guduvancheri', 'Nandura', 'Nandurbar',
          'Nandyal', 'Nangal', 'Nanjangud', 'Nanjikottai', 'Nanpara', 'Narasapuram', 'Narasaraopet', 'Naraura',
          'Narayanpet', 'Nargund', 'Narkatiaganj', 'Narkhed', 'Narnaul', 'Narsinghgarh', 'Narsinghgarh', 'Narsipatnam',
          'Narwana', 'Nashik', 'Nasirabad', 'Natham', 'Nathdwara', 'Naugachhia', 'Naugawan Sadat', 'Nautanwa',
          'Navalgund', 'Navi Mumbai', 'Navsari', 'Nawabganj', 'Nawada', 'Nawanshahr', 'Nawapur', 'Nedumangad',
          'Neem-Ka-Thana', 'Neemuch', 'Nehtaur', 'Nelamangala', 'Nellikuppam', 'Nellore', 'Nepanagar', 'New Delhi',
          'Neyveli (TS)', 'Neyyattinkara', 'Nidadavole', 'Nilanga', 'Nilambur', 'Nimbahera', 'Nirmal', 'Niwari',
          'Niwai', 'Nizamabad', 'Nohar', 'Noida', 'Nokha', 'Nokha', 'Nongstoin', 'Noorpur', 'North Lakhimpur',
          'Nowgong', 'Nowrozabad (Khodargama)', 'Nuzvid', "O' Valley", 'Oddanchatram', 'Obra', 'Ongole', 'Orai',
          'Osmanabad', 'Ottappalam', 'Ozar', 'P.N.Patti', 'Pachora', 'Pachore', 'Pacode', 'Padmanabhapuram', 'Padra',
          'Padrauna', 'Paithan', 'Pakaur', 'Palacole', 'Palai', 'Palakkad', 'Palani', 'Palanpur', 'Palasa Kasibugga',
          'Palghar', 'Pali', 'Pali', 'Palia Kalan', 'Palitana', 'Palladam', 'Pallapatti', 'Pallikonda', 'Palwal',
          'Palwancha', 'Panagar', 'Panagudi', 'Panaji', 'Panamattom', 'Panchkula', 'Panchla', 'Pandharkaoda',
          'Pandharpur', 'Pandhurna', 'Pandua', 'Panipat', 'Panna', 'Panniyannur', 'Panruti', 'Panvel', 'Pappinisseri',
          'Paradip', 'Paramakudi', 'Parangipettai', 'Parasi', 'Paravoor', 'Parbhani', 'Pardi', 'Parlakhemundi', 'Parli',
          'Partur', 'Parvathipuram', 'Pasan', 'Paschim Punropara', 'Pasighat', 'Patan', 'Pathanamthitta', 'Pathankot',
          'Pathardi', 'Pathri', 'Patiala', 'Patna', 'Pattran', 'Patratu', 'Pattamundai', 'Patti', 'Pattukkottai',
          'Patur', 'Pauni', 'Pauri', 'Pavagada', 'Pedana', 'Peddapuram', 'Pehowa', 'Pen', 'Perambalur', 'Peravurani',
          'Peringathur', 'Perinthalmanna', 'Periyakulam', 'Periyasemur', 'Pernampattu', 'Perumbavoor', 'Petlad',
          'Phagwara', 'Phalodi', 'Phaltan', 'Phillaur', 'Phulabani', 'Phulera', 'Phulpur', 'Phusro', 'Pihani', 'Pilani',
          'Pilibanga', 'Pilibhit', 'Pilkhuwa', 'Pindwara', 'Pinjore', 'Pipar City', 'Pipariya', 'Piro', 'Piriyapatna',
          'Pithampur', 'Pithapuram', 'Pithoragarh', 'Pollachi', 'Polur', 'Pondicherry', 'Ponnani', 'Ponneri', 'Ponnur',
          'Porbandar', 'Porsa', 'Port Blair', 'Powayan', 'Prantij', 'Pratapgarh', 'Pratapgarh', 'Prithvipur',
          'Proddatur', 'Pudukkottai', 'Pudupattinam', 'Pukhrayan', 'Pulgaon', 'Puliyankudi', 'Punalur', 'Punch', 'Pune',
          'Punjaipugalur', 'Punganur', 'Puranpur', 'Purna', 'Puri', 'Purnia', 'Purquazi', 'Purulia', 'Purwa', 'Pusad',
          'Puttur', 'Puthuppally', 'Puttur', 'Qadian', 'Koyilandy', 'Rabkavi Banhatti', 'Radhanpur', 'Rae Bareli',
          'Rafiganj', 'Raghogarh-Vijaypur', 'Raghunathpur', 'Raghunathganj', 'Rahatgarh', 'Rahuri', 'Raayachuru',
          'Raiganj', 'Raigarh', 'Ranebennuru', 'Ranipet', 'Raikot', 'Raipur', 'Rairangpur', 'Raisen', 'Raisinghnagar',
          'Rajagangapur', 'Rajahmundry', 'Rajakhera', 'Rajaldesar', 'Rajam', 'Rajampet', 'Rajapalayam', 'Rajauri',
          'Rajgarh (Alwar)', 'Rajgarh (Churu)', 'Rajgarh', 'Rajgir', 'Rajkot', 'Rajnandgaon', 'Rajpipla', 'Rajpura',
          'Rajsamand', 'Rajula', 'Rajura', 'Ramachandrapuram', 'Ramagundam', 'Ramanagaram', 'Ramanathapuram', 'Ramdurg',
          'Rameshwaram', 'Ramganj Mandi', 'Ramgarh', 'Ramngarh', 'Ramnagar', 'Ramnagar', 'Rampur', 'Rampur Maniharan',
          'Rampur Maniharan', 'Rampura Phul', 'Rampurhat', 'Ramtek', 'Ranaghat', 'Ranavav', 'Ranchi', 'Rangia', 'Rania',
          'Ranibennur', 'Rapar', 'Rasipuram', 'Rasra', 'Ratangarh', 'Rath', 'Ratia', 'Ratlam', 'Ratnagiri', 'Rau',
          'Raurkela', 'Raver', 'Rawatbhata', 'Rawatsar', 'Raxaul Bazar', 'Rayachoti', 'Rayadurg', 'Rayagada', 'Reengus',
          'Rehli', 'Renigunta', 'Renukoot', 'Reoti', 'Repalle', 'Revelganj', 'Rewa', 'Rewari', 'Rishikesh', 'Risod',
          'Robertsganj', 'Robertson Pet', 'Rohtak', 'Ron', 'Roorkee', 'Rosera', 'Rudauli', 'Rudrapur', 'Rudrapur',
          'Rupnagar', 'Sabalgarh', 'Sadabad', 'Sadalagi', 'Sadasivpet', 'Sadri', 'Sadulshahar', 'Sadulpur', 'Safidon',
          'Safipur', 'Sagar', 'Sagara', 'Sagwara', 'Saharanpur', 'Saharsa', 'Sahaspur', 'Sahaswan', 'Sahawar',
          'Sahibganj', 'Sahjanwa', 'Saidpur', 'Saiha', 'Sailu', 'Sainthia', 'Sakaleshapura', 'Sakti', 'Salaya', 'Salem',
          'Salur', 'Samalkha', 'Samalkot', 'Samana', 'Samastipur', 'Sambalpur', 'Sambhal', 'Sambhar', 'Samdhan',
          'Samthar', 'Sanand', 'Sanawad', 'Sanchore', 'Sarsod', 'Sindagi', 'Sandi', 'Sandila', 'Sanduru', 'Sangamner',
          'Sangareddy', 'Sangaria', 'Sangli', 'Sangole', 'Sangrur', 'Sankarankoil', 'Sankari', 'Sankeshwara',
          'Santipur', 'Sarangpur', 'Sardarshahar', 'Sardhana', 'Sarni', 'Sasaram', 'Sasvad', 'Satana', 'Satara',
          'Satna', 'Sathyamangalam', 'Sattenapalle', 'Sattur', 'Saunda', 'Saundatti-Yellamma', 'Sausar', 'Savarkundla',
          'Savanur', 'Savner', 'Sawai Madhopur', 'Sawantwadi', 'Sedam', 'Sehore', 'Sendhwa', 'Seohara', 'Seoni',
          'Seoni-Malwa', 'Shahabad', '"Shahabad', '"Shahabad', 'Shahade', 'Shahbad', 'Shahdol', 'Shahganj',
          'Shahjahanpur', 'Shahpur', 'Shahpura', 'Shahpura', 'Shajapur', 'Shamgarh', 'Shamli', '"Shamsabad',
          '"Shamsabad', 'Shegaon', 'Sheikhpura', 'Shendurjana', 'Shenkottai', 'Sheoganj', 'Sheohar', 'Sheopur',
          'Sherghati', 'Sherkot', 'Shiggaon', 'Shikaripur', '"Shikarpur', 'Shikohabad', 'Shillong', 'Shimla',
          'Shivamogga', 'Shirdi', 'Shirpur-Warwade', 'Shirur', 'Shishgarh', 'Shivpuri', 'Sholavandan', 'Sholingur',
          'Shoranur', 'Surapura', 'Shrigonda', 'Shrirampur', 'Shrirangapattana', 'Shujalpur', 'Siana', 'Sibsagar',
          'Siddipet', 'Sidhi', 'Sidhpur', 'Sidlaghatta', 'Sihor', 'Sihora', 'Sikanderpur', 'Sikandra Rao',
          'Sikandrabad', 'Sikar', 'Silao', 'Silapathar', 'Silchar', 'Siliguri', 'Sillod', 'Silvassa', 'Simdega',
          'Sindhagi', 'Sindhnur', 'Singrauli', 'Sinnar', 'Sira', 'Sircilla', 'Sirhind Fatehgarh Sahib', 'Sirkali',
          'Sirohi', 'Sironj', 'Sirsa', 'Sirsaganj', 'Sirsi', 'Sirsi', 'Siruguppa', 'Sitamarhi', 'Sitapur', 'Sitarganj',
          'Sivaganga', 'Sivagiri', 'Sivakasi', 'Siwan', 'Sohagpur', 'Sohna', 'Sojat', 'Solan', 'Solapur', 'Sonamukhi',
          'Sonepur', 'Songadh', 'Sonipat', 'Sopore', 'Soro', 'Soron', 'Soyagaon', 'Sri Madhopur', 'Srikakulam',
          'Srikalahasti', 'Srinagar', 'Srinagar', 'Srinivaspur', 'Srisailam Project (Right Flank Colony) Township',
          'Srirampore', 'Srivilliputhur', 'Suar', 'Sugauli', 'Sujangarh', 'Sujanpur', 'Sultanganj', 'Sullurpeta',
          'Sultanpur', 'Sumerpur', 'Sumerpur', 'Sunabeda', 'Sunam', 'Sundargarh', 'Sundarnagar', 'Supaul', 'Surandai',
          'Surat', 'Suratgarh', 'Suri', 'Suriyampalayam', 'Suryapet', 'Tadepalligudem', 'Tadpatri', 'Taki', 'Talaja',
          'Talcher', 'Talegaon Dabhade', 'Talikota', 'Taliparamba', 'Talode', 'Talwara', 'Tamluk', 'Tanda', 'Tandur',
          'Tanuku', 'Tarakeswar', 'Tarana', 'Taranagar', 'Taraori', 'Tarbha', 'Tarikere', 'Tarn Taran', 'Tasgaon',
          'Tehri', 'Tekkalakote', 'Tenali', 'Tenkasi', 'Tenu dam-cum-Kathhara', 'Terdal', 'Tezpur', 'Thakurdwara',
          'Thammampatti', 'Thana Bhawan', 'Thane', 'Thanesar', 'Thangadh', 'Thanjavur', 'Tharad', 'Tharamangalam',
          'Tharangambadi', 'Theni Allinagaram', 'Thirumangalam', 'Thirupuvanam', 'Thiruthuraipoondi', 'Thiruvalla',
          'Thiruvallur', 'Thiruvananthapuram', 'Thiruvarur', 'Thodupuzha', 'Thoubal', 'Thrissur', 'Thuraiyur',
          'Tikamgarh', 'Tilda Newra', 'Tilhar', 'Talikota', 'Tindivanam', 'Tinsukia', 'Tiptur', 'Tirora', 'Tiruchendur',
          'Tiruchengode', 'Tiruchirappalli', 'Tirukalukundram', 'Tirukkoyilur', 'Tirunelveli', 'Tirupathur',
          'Tirupathur', 'Tirupati', 'Tiruppur', 'Tirur', 'Tiruttani', 'Tiruvannamalai', 'Tiruvethipuram', 'Tiruvuru',
          'Tirwaganj', 'Titlagarh', 'Tittakudi', 'Todabhim', 'Todaraisingh', 'Tohana', 'Tonk', 'Tuensang', 'Tuljapur',
          'Tulsipur', 'Tumkur', 'Tumsar', 'Tundla', 'Tuni', 'Tura', 'Uchgaon', 'Udaipur', 'Udaipur', 'Udaipurwati',
          'Udgir', 'Udhagamandalam', 'Udhampur', 'Udumalaipettai', 'Udupi', 'Ujhani', 'Ujjain', 'Umarga', 'Umaria',
          'Umarkhed', 'Umbergaon', 'Umred', 'Umreth', 'Una', 'Unjha', 'Unnamalaikadai', 'Unnao', 'Upleta', 'Uran',
          'Uran Islampur', 'Uravakonda', 'Urmar Tanda', 'Usilampatti', 'Uthamapalayam', 'Uthiramerur', 'Utraula',
          'Vadakkuvalliyur', 'Vadalur', 'Vadgaon Kasba', 'Vadipatti', 'Vadnagar', 'Vadodara', 'Vaijapur', 'Vaikom',
          'Valparai', 'Valsad', 'Vandavasi', 'Vaniyambadi', 'Vapi', 'Vapi', 'Varanasi', 'Varkala', 'Vasai-Virar',
          'Vatakara', 'Vedaranyam', 'Vellakoil', 'Vellore', 'Venkatagiri', 'Veraval', 'Vidisha', '"Vijainagar',
          'Vijapur', 'Vijaypur', 'Vijayapura', 'Vijayawada', 'Vikarabad', 'Vikramasingapuram', 'Viluppuram',
          'Vinukonda', 'Viramgam', 'Virudhachalam', 'Virudhunagar', 'Visakhapatnam', 'Visnagar', 'Viswanatham', 'Vita',
          'Vizianagaram', 'Vrindavan', 'Vyara', 'Wadgaon Road', 'Wadhwan', 'Wadi', 'Wai', 'Wanaparthy', 'Wani',
          'Wankaner', 'Wara Seoni', 'Warangal', 'Wardha', 'Warhapur', 'Warisaliganj', 'Warora', 'Warud', 'Washim',
          'Wokha', 'Yadgir', 'Yamunanagar', 'Yanam', 'Yavatmal', 'Yawal', 'Yellandu', 'Yemmiganur', 'Yerraguntla',
          'Yevla', 'Zaidpur', 'Zamania', 'Zira', 'Zirakpur', 'Zunheboto']



def DetailExtractor(UserId):
    global Status_Collection
    global Information_Collection
    Items = {1: "Oxygen Cylinder", 2: "Hospital bed", 3: "Plasma", 4: "Remedisvir", 5: "Fabiflu", 6: "Tocilizumbad", 7: "Oxygen Refill"}
    Details = next(Information_Collection.find({'_id': UserId}))
    return 'Your following details are noted:'+'\nPatient Name: '+Details['Name']+'\nLocation: '+Details['Location']+'\nItem: '+ Items[int(Details['Item'])]+'\nPhone Number: '+ Details['Phone Number'] +'\n\nIf you wish to re-enter, type: deleteme'

def locator(location):
    global cities
    scores = []
    for city in cities:
        scores.append(difflib.SequenceMatcher(None, city, location).ratio())
    maximum = max(scores)
    index = 0
    for i in scores:
        if maximum == i:
            return cities[index]
        index += 1



def ValidateNumber(Number):
    if Number.isdigit():
        if int(Number) >= 7000000000 and int(Number) < 10000000000:
            return True
    return False


def SendMessage(UserId, content):
    return requests.get(url='https://api.telegram.org/' + 'bot1677533831:AAE6Pyz91cyqR-zUhJq-ksjo-x13tUx3-Uk' + '/sendMessage' + '?chat_id=' + str(UserId) + '&text=' + content)

def DetailRequired(UserId, Message):
    global Status_Collection
    global Information_Collection
    Status = next(Status_Collection.find({"_id": UserId}, {"Phone Number": 1, "Name": 1, "Location": 1, "Item": 1, "Completed": 1}))
    if Message == "deleteme" and Status["Completed"] == True:
        SendMessage(UserId, "All your current data has been erased. Please enter again if you wish.\n")
        Status_Collection.delete_one({"_id": {"$eq": UserId}})
        Information_Collection.delete_one({"_id": {"$eq": UserId}})
        return True

    if Status["Completed"] == True:
        return 0
    if Status['Phone Number'] == False: # Just receiving phone number
        if ValidateNumber(Message) == False:
            SendMessage(UserId, 'Incorrect phone number format. Please re-enter.')
            return 1
        else:
            Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Phone Number": True}})
            Information_Collection.insert_one({'_id': UserId, 'Phone Number': Message})
            return 2

    if Status["Name"] == False:
        Information_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Name": Message}})
        Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Name": True}})
        return 3

    if Status["Location"] == False:  # Just received location
        Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Location": True}})
        location_ofperson = locator(Message)
        Information_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Location": location_ofperson}})
        SendMessage(UserId, "Your location is noted as: "+location_ofperson)
        return 4

    if Status['Phone Number'] == True and Status["Name"] == True and Status["Location"] == True and Status["Item"] == False:
        if Message.isdigit():
            if int(Message) >= 1 and int(Message) <= 7:
                Information_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Item": int(Message)}})
                Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Item": True}})
                Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Completed": True}})
                return 0
        SendMessage(UserId, "Incorrect value, please re-enter.")
        return 4




def PhoneNumber(UserId):
    global Status_Collection
    global Information_Collection
    SendMessage(UserId, 'What is your phone number? (e.g. 9101234567)')
    if Status_Collection.count_documents({'_id': {"$in": [UserId]}}) == 0:
        Status_Collection.insert_one({"_id": UserId, "Phone Number": False, "Name": False, "Location": False, "Item": False, "Completed": False})
    else:
        Status_Collection.update_one({"_id": {"$eq": UserId}}, {"$set": {"Phone Number": False}})

def Name(UserId):
    SendMessage(UserId, "What is your name?")

def Location(UserId):  # 1. Put status as [item], 2. Ask for location
    SendMessage(UserId, "Which city are you in? (e.g. kolkata)")


def Item(UserId):  # 1. Put status as [], 2. Ask for item
    SendMessage(UserId, "Write the number of the item you need:\n1. Oxygen Cylinder\n2. Hospital bed\n3. Plasma\n4. Remedisvir\n5. Fabiflu\n6. Tocilizumbad\n7. Oxygen Refill\n")



def lambda_handler(event, context):
    if 'message' not in event:
        return {'statusCode': 200
                }
    global Status_Collection
    global Information_Collection
    global cities
    global client
    db = client.get_database('UserData')
    Status_Collection = db.get_collection("Status")
    Information_Collection = db.get_collection("Information")
    Data_Received = event
    UserId = Data_Received['message']['from']['id']
    Message = Data_Received['message']['text']
    if Status_Collection.count_documents({'_id': {"$in": [UserId]}}) == 0:
        detail = 1
    else:
        detail = DetailRequired(UserId, Message)
    if detail == 1:
        PhoneNumber(UserId)
    if detail == 2:
        Name(UserId)
    if detail == 3:
        Location(UserId)
    if detail == 4:
        Item(UserId)
    if detail == 0:
        SendMessage(UserId, DetailExtractor(UserId))
