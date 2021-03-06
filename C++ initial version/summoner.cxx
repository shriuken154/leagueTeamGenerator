#include "summoner.h"
#include "leagueEnum.h"
#include "string"
#include "iostream"

Summoner::Summoner():
sname("Default"), 
pname("Default"), 
league(LeagueEnums::unranked), 
division(1), 
primaryRole(LeagueEnums::noroll),
secndryRole(LeagueEnums::noroll)
{}

void Summoner::setSummonerName(const std::string& name){
    sname = name;
}

void Summoner::setPlayerName(const std::string& name){
    pname = name;
}

void Summoner::setLeague(const LeagueEnums::League newLeague){
    league = newLeague;
}

void Summoner::setDivision(const int div){
    division = div;
}

void Summoner::setPrimaryRole(LeagueEnums::Role prim){
    primaryRole = prim;
}

void Summoner::setSecndryRole(LeagueEnums::Role scnd){
    secndryRole = scnd;
}

std::string Summoner::getSummonerName() const{
    return sname;
}

std::string Summoner::getPlayerName() const{
    return pname;
}

LeagueEnums::League Summoner::getLeague() const{
    return league;
}

int Summoner::getDivision() const{
    return division;
}

int Summoner::getRank() const{
    //std::cout<<league<<std::endl;
    if (league == LeagueEnums::unranked or
        league == LeagueEnums::masters or 
        league == LeagueEnums::challenger){
        return league;
    }
    else{
        return league*5 - (5 - division);
    }
}

LeagueEnums::Role Summoner::getPrimaryRole() const{
    return primaryRole;
}

LeagueEnums::Role Summoner::getSecndryRole() const{
    return secndryRole;
}
