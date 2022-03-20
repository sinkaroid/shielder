#!/usr/bin/perl

use HTTP::Request;
use LWP::UserAgent;
use Term::ANSIColor;
my @c = ("\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[0;32m", "\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[0;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;34m");

system('clear');
system('cls');
system('title  Control Shell Finder');
system "color c";
print "                                 
 _        _                        _ 
| |_ ___ | |__  _ __ _   _   ____ | |
| __/ _ || '__|| '__| | | | | '_ || |
| || (_) | | | | |  | |_| |_| |_)|| |
|__|____||_| |_|_|  |__,_(_) .___/|_|
                            |_|      
        Shellfinder perlbased.
            [github/sinkaroid/tohru/json.txt] = current wordlist                                              
                                               ";

print "\n";
print $c[2]. "abandon all hope, ye who enter here";
print "\n";
print "\n";
print $c[5]. ">>> ";

$site="http://artbyronnierob.com/";


{print $c[2]. "\n";}


@path = (
'/mad.php',
'/oi.php',
'/anonymous.php',
'/madspotshell.php'
); #and so on...

foreach $myshell(@path){

$url = $site.$myshell;
$req = HTTP::Request->new(GET=>$url);
$useragent = LWP::UserAgent->new();

$response = $useragent->request($req);

if ($response->is_success){
print $c[3]. "\n200 => $url\n\n";
}else{
print $c[2]. "404 => $site$myshell\n";
}
}
