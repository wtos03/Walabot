import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { SocketcomPage } from './socketcom';

@NgModule({
  declarations: [
    SocketcomPage,
  ],
  imports: [
    IonicPageModule.forChild(SocketcomPage),
  ],
})
export class SocketcomPageModule {}
