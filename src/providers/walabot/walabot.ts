import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

/*
  Generated class for the WalabotProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/


@Injectable()
export class WalabotProvider {
  walabotArena = {
    radiusMin : 10,
    radiusMax : 100,
    thetaMin  : -45,
    thetaMax  : 45,
    phiMin    : -45,
    phiMax    : 45,
    radiusRes : 2,
    thetaRes  : 5,
    phiRes    : 5,
    mti       : true,
    threshold : 30,
    energythreshold : 10000
  }
  walabotAddress = {
//    ip        : "localhost",   // Walabot  IP  Address
    ip        : "192.168.100.140",   // Walabot  IP  Address
    port      :  8089
  }
  walabotAction = {
    ifKey     : "IFTTT KEY",
    iftttTrig : false,
    dPort     : true,
    aPort     : false,
    repeat    : "once",
    objDetect : "in"
  }
  //constructor(public http: HttpClient) {
  constructor() {
      console.log('Hello WalabotProvider Provider');
  }

}
