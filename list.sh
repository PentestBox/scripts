if [ $# -eq 0 ]
then
	echo -e "\e[36mHi there! Below is the list of tools which comes installed by default in PentestBox. You can check the alias by entering the commands given below."
	echo -e "\e[36mFor more information about tools usage, please visit tools.pentestbox.com"
	echo -e "\e[36m"
	echo -e "\e[32mlist android				Display aliases of Android Security Tools"
	echo -e "\e[34mlist forensic			Display aliases of Forensic Tools"
	echo -e "\e[37mlist informationgathering		Display aliases of Information Gathering Tools"
	echo -e "\e[35mlist passwordattacks			Display aliases of Password Attacks Tools"
	echo -e "\e[32mlist reverseengineering		Display aliases of Reverse Engineering Tools"
	echo -e "\e[34mlist stresstesting			Display aliases of Stress Testing Tools"
	echo -e "\e[37mlist sniffing			Display aliases of Sniffing Tools"
	echo -e "\e[31mlist webapplication			Display aliases of Web Application Tools"
	echo -en "\e[0m"
	exit
fi

if [ $1 = "webapplication" ]
then
	echo -e "\e[36malias				Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[31mburpsuite			Burp Suite"
	echo -e "\e[32mcommix				Commix"
  echo -e "\e[36mcmsmap				CMSmap"
  echo -e "\e[37mdotdotpwn			dotdotpwn"
	echo -e "\e[34mdirsearch			dirs3arch"
	echo -e "\e[36mdirbuster			DirBuster"
  echo -e "\e[32mdroopescan			Droopescan"
	echo -e "\e[37mfimap				fimap"
	echo -e "\e[35mgolismero			Golismero Project"
	echo -e "\e[31mjSQL				jSQL"
  echo -e "\e[32mjoomscan			OWASP Joomla Vulnerability Scanner"
	echo -e "\e[36mnikto				Nikto"
	echo -e "\e[31mpadbuster			Padbuster"
	echo -e "\e[32msqlmap				SQLmap"
	echo -e "\e[34mvega				Vega"
  echo -e "\e[32mvbscan				VbScan"
	echo -e "\e[37mwpscan				WpScan"
	echo -e "\e[36myasuo				Yasuo"
	echo -e "\e[31mzapd				Zaproxy"
	echo -en "\e[0m"
	exit
fi
if [ $1 = "informationgathering" ]
then
	echo -e "\e[36malias				Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[31mipscan				Angry IP Scanner"
	echo -e "\e[36mautomater			Automater"
	echo -e "\e[32mdnsrecon			DNSrecon"
	echo -e "\e[34mgolismero			Golismero Project"
	echo -e "\e[37minstarecon			Instarecon"
	echo -e "\e[35mknockpy				KnockPy"
	echo -e "\e[36mnmap				Nmap"
	echo -e "\e[36mncat				Netcat"
	echo -e "\e[36mndiff				A utility for comparing Nmap scan results"
	echo -e "\e[36mnping				Network packet generation tool / ping utiliy-Nmap"
	echo -e "\e[31mresponder			Responder"
	echo -e "\e[32msnmpwalk			SnmpWalk"
  echo -e "\e[33mspiderfoot			SpiderFoot"
	echo -e "\e[37msslstrip			SSLStrip"
	echo -e "\e[35msslyze				SSLyze"
	echo -e "\e[36msslscan				SSLScan"
	echo -e "\e[31msubbrute			SubBrute"
  echo -e "\e[37msublist3r			Sublist3r"
  echo -e "\e[32mtestsslserver			TestSSLServer"
	echo -e "\e[36murlcrazy			UrlCrazy"
	echo -e "\e[31mtheHarveser			The Harvester"
	echo -e "\e[32mwireshark			Wireshark"
	echo -en "\e[0m"
	exit
fi
if [ $1 = "passwordattacks" ]
then
	echo -e "\e[36malias			Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[32mburpsuite		Burp Suite"
	echo -e "\e[37mfindmyhash		Find My Hash"
	echo -e "\e[34mhashidentifier		Hash Identifier"
	echo -e "\e[37mhashcat-cli32		Hashcat"
	echo -e "\e[35mhashcat-cli64		Hashcat"
	echo -e "\e[36mhashcat-cliXOP		Hashcat"
	echo -e "\e[31mlazagne			LaZagne"
	echo -e "\e[36mjohntheripper		John The Ripper"
	echo -e "\e[31mpatator			Patator"
	echo -e "\e[32mrcrack			RainbowCrack"
	echo -e "\e[32mrt2rtc			RainbowCrack"
	echo -e "\e[32mrtc2rt			RainbowCrack"
	echo -e "\e[32mrtgen			RainbowCrack"
	echo -e "\e[32mrtsort			RainbowCrack"
	echo -e "\e[34mhydra			Thc Hydra"
	echo -e "\e[37mzap			Zaproxy"
	echo -en "\e[0m"
	exit
fi
if [ $1 = "android" ]
then
	echo -e "\e[36malias			Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[37mandroapkinfo		Androguard"
	echo -e "\e[37mandroarsc		Androguard"
	echo -e "\e[37mandroauto		Androguard"
	echo -e "\e[37mandroxml		Androguard"
	echo -e "\e[37mandrocsign		Androguard"
	echo -e "\e[37mandrodd			Androguard"
	echo -e "\e[37mandrodiff		Androguard"
	echo -e "\e[37mandrodis		Androguard"
	echo -e "\e[37mandrogui		Androguard"
	echo -e "\e[36mandrowarn		Androwarn"
  echo -e "\e[32mandrobugs		AndroBugs Framework"
	echo -e "\e[31mapktool			Apktool"
  echo -e "\e[36mbytecodeviewer		ByteCodeViewer"
	echo -e "\e[32md2j-dex2jar		dexjar"
	echo -e "\e[34mdrozer			Drozer"
	echo -e "\e[37mintrospy		Introspy-Analyzer"
	echo -e "\e[35mjdgui			JD-GUI"
	echo -e "\e[36mpidcat			Pidcat"
	echo -e "\e[31m"
	echo -en "\e[0m"
	exit
fi
if [ $1 = "reverseengineering" ]
then
	echo -e "\e[36malias				Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[37mapktool				ApkTool"
	echo -e "\e[35mdex2jar				dex2jar"
	echo -e "\e[35mjad				Jad"
	echo -e "\e[36mjdgui				JD-GUI"
	echo -e "\e[31mjavasnoop			JavaSnoop"
	echo -e "\e[36mollydbg				OLLY Debugger"
	echo -e "\e[31mradare2				Radare2. Please check tools.pentestbox.com for more info."
	echo -en "\e[0m"
	exit
fi

if [ $1 = "stresstesting" ]
then
	echo -e "\e[36malias			Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[31mthc-ssl-dos		THC-SSL-DOS"
	echo -en "\e[0m"
	exit
fi
if [ $1 = "sniffing" ]
then
	echo -e "\e[36malias			Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[31mburpsuite		Burp Suite"
	echo -e "\e[32mdnschef			DNSchef"
	echo -e "\e[34mettercap		EtterCap"
  echo -e "\e[32mngrep			Ngrep"
  echo -e "\e[36mnetworkminer		NetworkMiner"
	echo -e "\e[37mresponder		Responder"
	echo -e "\e[35msslstrip		SSLStrip"
  echo -e "\e[32mwindump			Windump"
	echo -e "\e[36mwireshark		Wireshark"
	echo -e "\e[31mzap			Zaproxy"
	echo -en "\e[0m"
	exit
fi

if [ $1 = "forensic" ]
then
	echo -e "\e[36malias			Tool/Product Name"
	echo -e "\e[36m"
	echo -e "\e[32mbulkextractor		Bulk Extractor"
	echo -e "\e[34mcaptipper		CapTipper"
	echo -e "\e[37mdumpzilla		DumpZilla"
	echo -e "\e[35mloki			Loki"
	echo -e "\e[36mmake-pdf-embeddded	Make PDF Tools"
	echo -e "\e[31mmake-pdf-javascript	Make PDF Tools"
	echo -e "\e[36mpdfsh			Origami"
	echo -e "\e[32mpedump			pedump"
	echo -e "\e[34mpdf-parser		PDF Parser"
	echo -e "\e[37mpdfid			PDF ID"
	echo -e "\e[35mpeepdf			PeePDF"
	echo -e "\e[36mrekall			Rekall"
	echo -e "\e[31mvolatility		Volatility"
	echo -en "\e[0m"
	exit
fi
