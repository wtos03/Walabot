import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { WalabotProvider } from '../../providers/walabot/walabot';

@Component({
  selector: 'page-config',
  templateUrl: 'config.html'
})
export class ConfigPage {

  wip = "192.168.100.140";
  wport = 8089;
  constructor(public navCtrl: NavController, public walabot: WalabotProvider) {

  }
  upDate(){
        this.walabot.setipaddress(this.wip);
        this.walabot.arena.port = this.wport;

  }

}
