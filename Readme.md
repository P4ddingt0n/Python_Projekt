Vi fick ett projekt vi ska göra. Här är dagbok och problem vi stötte på.

Först diskuterade vi vad vi skulle hitta på. Vi valde nummer 2 av dom 3 projekten.


Först fick vi skapa en fil som skulle användas som en tabell scriptet kan läsa av, en såkallad csv fil. Vi hade lite problem med att få scriptet att läsa filen vi skapade med tabellen. Efter lite små pill och justering i scriptet att ta bort ett mellanslag och byta ut tabell.csv mot det riktiga filnamnet.

Regel:1
SSH här fick vi använda en färdig running config från ett nätverk för att få fram med ett script att den skall läsa av att det finns ssh aktiverat.
Resultatet blev att den kunde inte hitta en ssh config. Så scriptet fungerar som det skall. Det som vi hade lite små justeringar som att få igång att den skall
filen i directory.

Regel:2
Det andra scriptet vi gjorde var ett script som scannar efter existerande VLAN och printar ut de VLAN som finns tillgängliga. Finns inga vlan tillgängliga så printar den "No VLAN found in running-config".

Regel:3
Därefter gjorde vi ett script som läser av vilka DHCP-pooler som finns konfigurerade, vilken nätverksadress, default-router och nätmask samtliga har.

Regel:4 
Det sista scriptet letar efter trunkar på nätverket, berättar vilken interface som Trunken sitter på och vilka VLAN som har tillåtelse att skicka paket över trunken.
