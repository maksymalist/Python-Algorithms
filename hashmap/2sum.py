import enum


def twoSum(nums, target):
    
    hm = {}
    
    for i, n in enumerate(nums):
        
        diff = target - n
        
        if diff in hm:
            return [hm[diff], i]
        
        hm[n] = i
    
arr = [-1158379,3950888,-6939762,-5333138,3403348,7898812,6236179,9848562,6720555,4059431,-73567,-866804,-7297520,-2898816,-7172867,1080540,-3227104,-7679368,-4957302,-3082798,-8621210,-6809020,8098838,8335693,-8411514,9211576,-1061148,8056513,-7639229,3794047,-6357974,-1434968,3544382,279308,5021399,-4117906,6205027,477729,2872711,6111196,-6216806,-1684906,3470212,-3650538,-7184069,-4472343,-2371219,-2872226,-2726472,5859318,-261557,-1831278,2389152,-1256128,-3835093,4004878,-6014522,-9447233,-9004312,7539214,3973608,9105973,-121579,6482179,-6760888,-5283207,3652454,-533533,3823972,6958976,-1577834,-5322656,-5084063,1669689,-2037349,6313475,-3955388,-1299352,-8207827,9573671,-1374884,1328920,-4690934,-6235939,-578055,-2319488,-8688747,2986621,6949206,6976965,-7603719,-3645952,-7730066,-4492729,2564530,4439780,606575,-1835755,-4637650,7475527,-9421766,5956519,-4207540,-9378884,-6516417,-798489,6977947,7273271,9418176,-3512546,-145011,8594515,-3942780,7009536,1070519,-941430,7480742,-2542949,-5444283,-7567348,-1515470,2047767,-1619087,1864295,4333979,7816882,-608594,7067056,-1430623,-7163293,-7912589,-4463672,-8828615,8678507,-2964776,4457870,8817531,747586,1987739,-3410791,-9943342,-357376,3922530,8533760,-6351160,-4278014,7242057,-1446527,1072694,-4598451,-2579089,-7623714,-5968754,3707522,-1079090,8451726,6526828,-6174288,427599,-4658129,-2597643,-1123665,9141014,647793,-3915711,6129747,9781024,7590067,-8874688,-2678942,5155179,377933,-702127,6884696,8064234,1767443,-3152841,1836312,-856548,-1565186,-6591567,-4790996,-991029,-6004969,3852799,-187586,-2831755,-9748605,-7088426,-4904197,-1408071,1865191,-7162533,7585917,-7243487,6092054,7792991,-3644463,2549608,-5146381,-7203771,5383449,4448534,3951781,3778824,-5665648,-2826395,3750222,2091716,5202513,807693,-8970897,5252667,-9752941,7495008,2746442,-2560072,-615148,-8961837,1094999,-6351747,-8351784,-2812864,-6991033,2149807,-1949824,3743059,-2634317,53822,8286306,6029840,-4802479,-5345412,-9710671,-7511534,-2872857,7998903,2379329,905794,954,-6048330,-4689992,9665771,1892961,-8932466,1277548,9951677,6200470,4487990,4552317,-5387992,-3228201,-4268055,-2558963,-1546961,9590555,7379574,7995160,-9299428,-8785863,6513453,-2190346,-6030777,-9079464,6048131,8309699,-9261452,4813954,1107555,-3048874,-3165967,4856558,-9313850,-904741,-3119997,-1582303,9270758,3489942,-4679112,-5374536,508173,-4032416,8651054,9627829,-360051,9738685,4884092,9831357,455209,907113,8567109,8649944,4215808,-6607358,3520130,4540007,7607151,-4139165,4462978,5231666,-5077063,2993866,7660335,8490802,-8426598,8175458,7267081,4711034,-2417193,-291956,3260247,2315251,-4795837,459720,-9622933,-5313904,6825276,-6153519,-577783,-7251682,5358329,-8984096,-2569907,8624201,-5402857,1301932,9842509,9158324,-4586424,3786819,3712671,-6802827,683430,4384775,-1388267,5920679,-9709472,3776941,137291,-1049933,1039964,-489286,8612445,-3666684,-5463920,953079,8611343,-6123289,2058046,3642876,-3199988,-7678779,-2490273,1439216,5007767,-8200972,-7296964,-5612240,8569099,-6699548,6177004,-6211374,-4310767,3456782,1115515,-6339554,-5944753,-6858186,1713590,8505342,-9193008,4155741,4427179,3794687,9076176,-3108339,-1479764,531982,6563004,-9300450,8087174,-5881942,4663978,6880161,-7949895,-168460,-3643205,975933,-4922088,-9856200,-2851138,-2382348,-2131881,-3802040,-1815701,6671801,4715587,5991026,4282889,-4192098,9915336,-9744419,-9878566,-5740362,-5428640,6767953,-3042885,-3909058,7796524,5681084,7646794,3389731,-4008642,2000681,6796532,7394912,-3798616,-3976088,-3563214,857212,-1186732,-2662363,-7898528,3384709,6352002,-7496384,-4205854,9815507,2181190,4922626,2169751,7484314,-8366983,-5654092,-8646750,9894585,-6709964,1954825,8038750,-3086673,241099,-9298149,8818314,700982,-8169796,4667448,5384189,-2411605,-3854789,4188763,-8652289,-3583616,5766361,-6348716,1050446,-305844,-6334452,-3822855,8447194,1102962,5222419,-5626219,-6792195,-2847496,1049562,4268832,-784299,-4544708,7120514,8115391,7315250,-2810200,-7238242,-7022454,8247777,-4351293,-4469888,9633701,-411513,-9567063,2296352,-2963878,584164,-30397,-1662533,-3291206,-7513862,4473262,-4517566,5172049,-1874532,-8592328,3897349,-630092,1879904,8305771,9435328,-8616093,-7598959,-6696362,615049,-7347243,7033113,-9739543,9571919,3879820,-8980076,8582214,-3022246,589157,-5384823,357106,-4103480,4386734,2204453,2598321,6279096,4417093,-5663228,-9114301,-2804160,-4167858,253781,2457391,2678500,6750900,9017732,-49436,-7226278,-4912013,7665340,-9854928,-6435774,-9974921,8759468,-3311164,-2887863,9099837,9685492,-5913757,5018970,-4772377,-2681605,-581247,9297706,546542,-7305693,-3811584,-8285866,-5054199,6664321,-3633430,4241844,8699262,1266653,-9379524,5422713,-5999284,2157609,-8081228,-2864818,-1791965,1677654,6273229,1771810,17420,-665350,8512206,5321681,8366760,-1769353,8307565,-6392754,5875574,-3744183,-9379269,-2040792,9171183,-3667801,3711699,3756818,-3159759,-6889931,-7818670,4419887,7807185,-5918410,3983386,-8060973,1599422,944788,-1875812,9041051,-4275111,-7739195,9766827,-5696823,-221211,4124487,-2694563,2875036,8419714,1404676,6127969,-9163901,2760485,-717724,-2755852,-4521939,-1270034,9014054,8511494,6041680,7072599,8069383,-336309,-841321,-2029079,-1844400,6717666,1806194,-7226070,-7653561,1480429,457986,-9317289,-1423228,-4185044,-5033300,6109753,-6227268,-7909810,606954,-544730,-9496571,-6809577,1175582,-6864921,-5049662,6337230,8323073,-1471044,8007193,2523019,-4239500,9086745,2216305,-5588337,-3870192,-5496725,-2206069,9748125,-878241,-3839658,7666265,2079681,8840474,-5776275,-6656276,-2756138,-6090025,1493043,-3217220,8218647,7264842,-2744404,-8923097,1930865,6605212,933242,8289045,2286807,-5254057,-1104116,-4605201,-6097717,-7049177,-3247240,-2421433,-9211067,-5945689,2851449,-2169494,8891236,-8435256,-3603846,-3635247,1483542,-9151188,1639086,8219731,-58127,4439787,476115,-1221293,4402701,-8198255,3543018,8396015,5496967,7965371,1613058,-824927,-8788304,-3027781,363776,-6493750,5021278,3092034,-8122137,45270,-9292776,4148342,-6030042,2561920,6430171,-6877552,-9718837,-9667026,-8832112,-6558660,5902739,-4855522,-2002676,4337335,-8116506,5653598,-6974233,382978,7259510,-8498840,3092980,2472678,8331323,-5807585,5423929,1020972,-2302809,-4312498,-7745276,4860081,-4210945,6192881,-64290,2314265,5342964,-6007705,-1383228,-8345152,-1036073,8672882,5110465,-5707834,1298170,-4458566,-1856272,-5305966,-8129919,8857103,-2843231,8059151,813224,2220445,4332898,8956358,1974355,3460513,-1747493,877163,-5993781,7990747,-8699805,-1326950,8380261,4018355,-8618029,-1532734,-4518024,9115099,8757866,-4530971,4214966,5873474,-7672423]
target = 2792509
print(twoSum(arr, target))