import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { WalabotProvider } from '../../providers/walabot/walabot';


@Component({
  selector: 'page-action',
  templateUrl: 'action.html'
})
export class ActionPage {

   tifttt = true;
   dport  = true;
   aport  = false;
   repeat = "once";
   detectobj = "in";


  constructor(public navCtrl: NavController,public walabot: WalabotProvider) {

  }
  apply(){
    this.walabot.walabotAction.iftttTrig = this.tifttt;
    this.walabot.walabotAction.dPort = this.dport;
    this.walabot.walabotAction.aPort = this.aport;
    this.walabot.walabotAction.repeat = this.repeat;
    this.walabot.walabotAction.objDetect = this.detectobj;

  }

  ionViewWillLeave()
  {
    this.apply();
  }
  
}
