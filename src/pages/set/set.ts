import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Socket } from 'ng-socket-io';
import { WalabotProvider } from '../../providers/walabot/walabot';


@Component({
  selector: 'page-set',
  templateUrl: 'set.html'
})
export class SetPage {
  
 /* wallabot = {
       radiusMin : 10,
       radiusMax : 100
  }
  */
  radius: any = { lower: 1, upper: 100 };
  theta: any = { lower: 0, upper: 90 };
  phi: any = { lower: 0, upper: 90 };
  mti = true;
  threshold: number;
  
  constructor(public navCtrl: NavController, public socket: Socket, public walabot: WalabotProvider ) {

  }
  sendCMD() {
    this.socket.connect();
    this.walabot.arena.radiusMax = this.radius.upper;
    this.socket.emit('message', this.walabot)
 //   this.navCtrl.push('SocketcomPage', { nickname: this.nickname });
  }       

}
