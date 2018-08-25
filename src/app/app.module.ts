import { NgModule, ErrorHandler } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { IonicApp, IonicModule, IonicErrorHandler } from 'ionic-angular';
import { MyApp } from './app.component';

import { ActionPage } from '../pages/action/action';
import { ConfigPage } from '../pages/config/config';
import { SetPage } from '../pages/set/set';
import { TabsPage } from '../pages/tabs/tabs';

import { StatusBar } from '@ionic-native/status-bar';
import { SplashScreen } from '@ionic-native/splash-screen';
import { SocketIoModule, SocketIoConfig } from 'ng-socket-io';

// Name space for using multiple socket on same Physical socket  host:port/namespace
// const config: SocketIoConfig = { url: 'http://192.168.100.140:8089/test', options: {} };
const config: SocketIoConfig = { url: 'http://localhost:8089', options: {} };

@NgModule({
  declarations: [
    MyApp,
    ActionPage,
    ConfigPage,
    SetPage,
    TabsPage
  ],
  imports: [
    BrowserModule,
    SocketIoModule.forRoot(config),  
    IonicModule.forRoot(MyApp)
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    ActionPage,
    ConfigPage,
    SetPage,
    TabsPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
