import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Socket } from 'ng-socket-io';


@Component({
  selector: 'page-set',
  templateUrl: 'set.html'
})
export class SetPage {
  
  radius: any = { lower: 1, upper: 100 };
  theta: any = { lower: 0, upper: 90 };
  phi: any = { lower: 0, upper: 90 };

  nickname = '';
  constructor(public navCtrl: NavController, public socket: Socket) {

  }
  sendCMD() {
    this.socket.connect();
    this.socket.emit('message', this.radius.upper);
 //   this.navCtrl.push('SocketcomPage', { nickname: this.nickname });
  }       

}
