import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Socket,SocketIoConfig} from 'ng-socket-io';
import { WalabotProvider } from '../../providers/walabot/walabot';


@Component({
  selector: 'page-set',
  templateUrl: 'set.html'
})
export class SetPage {
  
 
  radius: any = { lower: this.walabot.walabotArena.radiusMin, upper: this.walabot.walabotArena.radiusMax };
  theta: any = { lower: this.walabot.walabotArena.thetaMin, upper: this.walabot.walabotArena.thetaMax };
  phi: any = { lower: this.walabot.walabotArena.phiMin, upper: this.walabot.walabotArena.phiMax };
  mti       = this.walabot.walabotArena.mti;
  threshold = this.walabot.walabotArena.threshold;
  enthreshold = this.walabot.walabotArena.energythreshold;
  jsontext: string;
  socket : Socket;
  ip: any;
  port : any;
  config: any;
  address: any;
 
 
  constructor(public navCtrl: NavController, public walabot: WalabotProvider ) {    
 // constructor(public navCtrl: NavController, public socket : Socket, public walabot: WalabotProvider ) {
    
  this.ip = this.walabot.walabotAddress.ip;
  this.port = this.walabot.walabotAddress.port;
  this.address = 'http://'+this.ip+':'+this.port;
  this.config = {url : this.address, options :  {}};
  this.socket = new Socket(this.config);

  }

  // Need to put socket here. Because we can change the ip:port from config page and connect to new socket
  // Any problem on memory leak on new Socket ??? don't know just note

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
    this.jsontext = JSON.stringify(this.walabot);
    this.socket.emit('message', this.jsontext);
  
  }     

}
