import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Socket } from 'ng-socket-io';
import { WalabotProvider } from '../../providers/walabot/walabot';


@Component({
  selector: 'page-set',
  templateUrl: 'set.html'
})
export class SetPage {
  
 
  radius: any = { lower: 1, upper: 100 };
  theta: any = { lower: 0, upper: 90 };
  phi: any = { lower: 0, upper: 90 };
  mti       = true;
  threshold = 30;
  enthreshold = 100;

  jsontext: string;
  
  constructor(public navCtrl: NavController, public socket: Socket, public walabot: WalabotProvider ) {

  }
  sendCMD() {

    this.socket.connect();
    this.walabot.walabotArena.radiusMin = this.radius.lower;
    this.walabot.walabotArena.radiusMax = this.radius.upper;
    this.walabot.walabotArena.phiMin  = this.phi.lower;
    this.walabot.walabotArena.phiMax  = this.phi.upper;
    this.walabot.walabotArena.thetaMin = this.theta.lower;
    this.walabot.walabotArena.thetaMax = this.theta.upper;
    this.walabot.walabotArena.mti = this.mti;
    this.walabot.walabotArena.threshold = this.threshold;
    this.walabot.walabotArena.energythreshold = this.enthreshold;
    this.jsontext = JSON.stringify(this.walabot)
    this.socket.emit('message', this.jsontext)
 //   this.navCtrl.push('SocketcomPage', { nickname: this.nickname });
  }       

}
