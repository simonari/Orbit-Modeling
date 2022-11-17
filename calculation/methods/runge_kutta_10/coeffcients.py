from numpy import array
from numpy import float64 as float

alphas = array([
    0.000000000000000000000000000000000000000000000000000000000000,
    0.100000000000000000000000000000000000000000000000000000000000,
    0.539357840802981787532485197881302436857273449701009015505500,
    0.809036761204472681298727796821953655285910174551513523258250,
    0.309036761204472681298727796821953655285910174551513523258250,
    0.981074190219795268254879548310562080489056746118724882027805,
    0.833333333333333333333333333333333333333333333333333333333333,
    0.354017365856802376329264185948796742115824053807373968324184,
    0.882527661964732346425501486979669075182867844268052119663791,
    0.642615758240322548157075497020439535959501736363212695909875,
    0.357384241759677451842924502979560464040498263636787304090125,
    0.117472338035267653574498513020330924817132155731947880336209,
    0.833333333333333333333333333333333333333333333333333333333333,
    0.309036761204472681298727796821953655285910174551513523258250,
    0.539357840802981787532485197881302436857273449701009015505500,
    0.100000000000000000000000000000000000000000000000000000000000,
    1.00000000000000000000000000000000000000000000000000000000000
], dtype=float)

cs = array([
    0.0333333333333333333333333333333333333333333333333333333333333,
    0.0250000000000000000000000000000000000000000000000000000000000,
    0.0333333333333333333333333333333333333333333333333333333333333,
    0.000000000000000000000000000000000000000000000000000000000000,
    0.0500000000000000000000000000000000000000000000000000000000000,
    0.000000000000000000000000000000000000000000000000000000000000,
    0.0400000000000000000000000000000000000000000000000000000000000,
    0.000000000000000000000000000000000000000000000000000000000000,
    0.189237478148923490158306404106012326238162346948625830327194,
    0.277429188517743176508360262560654340428504319718040836339472,
    0.277429188517743176508360262560654340428504319718040836339472,
    0.189237478148923490158306404106012326238162346948625830327194,
    -0.0400000000000000000000000000000000000000000000000000000000000,
    -0.0500000000000000000000000000000000000000000000000000000000000,
    -0.0333333333333333333333333333333333333333333333333333333333333,
    -0.0250000000000000000000000000000000000000000000000000000000000,
    0.0333333333333333333333333333333333333333333333333333333333333
], dtype=float)

betas = array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.100000000000000000000000000000000000000000000000000000000000,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-0.915176561375291440520015019275342154318951387664369720564660,
     1.45453440217827322805250021715664459117622483736537873607016,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.202259190301118170324681949205488413821477543637878380814562,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.606777570903354510974045847616465241464432630913635142443687,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.184024714708643575149100693471120664216774047979591417844635,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.197966831227192369068141770510388793370637287463360401555746,
     -0.0729547847313632629185146671595558023015011608914382961421311,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.0879007340206681337319777094132125475918886824944548534041378,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.410459702520260645318174895920453426088035325902848695210406,
     0.482713753678866489204726942976896106809132737721421333413261,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.0859700504902460302188480225945808401411132615636600222593880,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.330885963040722183948884057658753173648240154838402033448632,
     0.489662957309450192844507011135898201178015478433790097210790,
     -0.0731856375070850736789057580558988816340355615025188195854775,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.120930449125333720660378854927668953958938996999703678812621,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.260124675758295622809007617838335174368108756484693361887839,
     0.0325402621549091330158899334391231259332716675992700000776101,
     -0.0595780211817361001560122202563305121444953672762930724538856,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.110854379580391483508936171010218441909425780168656559807038,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.0605761488255005587620924953655516875526344415354339234619466,
     0.321763705601778390100898799049878904081404368603077129251110,
     0.510485725608063031577759012285123416744672137031752354067590,
     0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.112054414752879004829715002761802363003717611158172229329393,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.144942775902865915672349828340980777181668499748506838876185,
     -0.333269719096256706589705211415746871709467423992115497968724,
     0.499269229556880061353316843969978567860276816592673201240332,
     0.509504608929686104236098690045386253986643232352989602185060,
     0, 0, 0, 0, 0, 0, 0, 0],
    [0.113976783964185986138004186736901163890724752541486831640341,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.0768813364203356938586214289120895270821349023390922987406384,
     0.239527360324390649107711455271882373019741311201004119339563,
     0.397774662368094639047830462488952104564716416343454639902613,
     0.0107558956873607455550609147441477450257136782823280838547024,
     -0.327769124164018874147061087350233395378262992392394071906457,
     0, 0, 0, 0, 0, 0, 0],
    [0.0798314528280196046351426864486400322758737630423413945356284,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.0520329686800603076514949887612959068721311443881683526937298,
     -0.0576954146168548881732784355283433509066159287152968723021864,
     0.194781915712104164976306262147382871156142921354409364738090,
     0.145384923188325069727524825977071194859203467568236523866582,
     -0.0782942710351670777553986729725692447252077047239160551335016,
     -0.114503299361098912184303164290554670970133218405658122674674,
     0, 0, 0, 0, 0, 0],
    [0.985115610164857280120041500306517278413646677314195559520529,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.330885963040722183948884057658753173648240154838402033448632,
     0.489662957309450192844507011135898201178015478433790097210790,
     -1.37896486574843567582112720930751902353904327148559471526397,
     -0.861164195027635666673916999665534573351026060987427093314412,
     5.78428813637537220022999785486578436006872789689499172601856,
     3.28807761985103566890460615937314805477268252903342356581925,
     -2.38633905093136384013422325215527866148401465975954104585807,
     -3.25479342483643918654589367587788726747711504674780680269911,
     -2.16343541686422982353954211300054820889678036420109999154887,
     0, 0, 0, 0, 0],
    [0.895080295771632891049613132336585138148156279241561345991710,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.197966831227192369068141770510388793370637287463360401555746,
     -0.0729547847313632629185146671595558023015011608914382961421311,
     0.0000000000000000000000000000000000000000000000000000000000000,
     -0.851236239662007619739049371445966793289359722875702227166105,
     0.398320112318533301719718614174373643336480918103773904231856,
     3.63937263181035606029412920047090044132027387893977804176229,
     1.54822877039830322365301663075174564919981736348973496313065,
     -2.12221714704053716026062427460427261025318461146260124401561,
     -1.58350398545326172713384349625753212757269188934434237975291,
     -1.71561608285936264922031819751349098912615880827551992973034,
     -0.0244036405750127452135415444412216875465593598370910566069132,
     0, 0, 0, 0],
    [-0.915176561375291440520015019275342154318951387664369720564660,
     1.45453440217827322805250021715664459117622483736537873607016,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.777333643644968233538931228575302137803351053629547286334469,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.0910895662155176069593203555807484200111889091770101799647985,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.0910895662155176069593203555807484200111889091770101799647985,
     0.777333643644968233538931228575302137803351053629547286334469,
     0, 0, 0],
    [0.100000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     -0.157178665799771163367058998273128921867183754126709419409654,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.157178665799771163367058998273128921867183754126709419409654,
     0, 0],
    [0.181781300700095283888472062582262379650443831463199521664945,
     0.675000000000000000000000000000000000000000000000000000000000,
     0.342758159847189839942220553413850871742338734703958919937260,
     0.000000000000000000000000000000000000000000000000000000000000,
     0.259111214548322744512977076191767379267783684543182428778156,
     -0.358278966717952089048961276721979397739750634673268802484271,
     -1.04594895940883306095050068756409905131588123172378489286080,
     0.930327845415626983292300564432428777137601651182965794680397,
     1.77950959431708102446142106794824453926275743243327790536000,
     0.100000000000000000000000000000000000000000000000000000000000,
     -0.282547569539044081612477785222287276408489375976211189952877,
     -0.159327350119972549169261984373485859278031542127551931461821,
     -0.145515894647001510860991961081084111308650130578626404945571,
     -0.259111214548322744512977076191767379267783684543182428778156,
     -0.342758159847189839942220553413850871742338734703958919937260,
     -0.675000000000000000000000000000000000000000000000000000000000,
     0],
])

print(alphas.shape)
print(cs.shape)
print(betas.shape)
