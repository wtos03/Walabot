import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

/*
  Generated class for the WalabotProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
@Injectable()
export class WalabotProvider {
  arena = {
    radiusMin : 10,
    radiusMax : 100,
    thetaMin  : -45,
    thetaMax  : 45,
    phiMin    : -45,
    phiMax    : 45,
    mti       : true,
    threshold : 200,
    ip        : "192.168.100.140",   // Walabot  IP  Address
    port      :  8089
  }
  constructor() {
    console.log('Hello WalabotProvider Provider');
    this.arena.radiusMax = 100;
    this.arena.radiusMin = 1;
  }
  setipaddress (ipa)
  {
    this.arena.ip = ipa;
  }

}
