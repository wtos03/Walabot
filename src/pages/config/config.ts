import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { WalabotProvider } from '../../providers/walabot/walabot';

@Component({
  selector: 'page-config',
  templateUrl: 'config.html'
})
export class ConfigPage {

 // wip = "192.168.100.140";
  wip = this.walabot.walabotAddress.ip;
  wport = this.walabot.walabotAddress.port;
  radiusres = 2;
  thetares = 5;
  phires = 5;
  ifkey = "cHnv9dt3W9X6bmF2vXn2r1";
  onlyread = false;
  
  constructor(public navCtrl: NavController, public walabot: WalabotProvider) {

  }
  upDate(){

        this.walabot.walabotAddress.ip = this.wip;
        this.walabot.walabotAddress.port = this.wport;
        this.walabot.walabotArena.radiusRes = this.radiusres;
        this.walabot.walabotArena.phiRes  = this.phires;
        this.walabot.walabotArena.thetaRes = this.thetares;
        this.walabot.walabotAction.ifKey = this.ifkey;
  }
  ionViewWillLeave()
  {
    this.upDate();
    this.onlyread = true;
    
  }

}
