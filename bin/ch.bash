#!/bin/bash
putong="cat tempres200"
kuntol="cat bajing.bash"
del="rm bajing.bash mek.bash"

${putong} | sed 's/OK//' | sed 's/\[\] : //' > bajing.bash
${kuntol} | sed 's/htt/curl -LI htt/' | sed "s/$/ -o \/dev\/null -w '%{http_code} => %{url_effective}\n' -s/" > mek.bash

bash mek.bash > lacur.log
${del}
#./basename(__FILE__) if only on your console, not discord