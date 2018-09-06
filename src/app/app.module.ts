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
import { WalabotProvider } from '../providers/walabot/walabot';


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
    {provide: ErrorHandler, useClass: IonicErrorHandler},
    WalabotProvider
  ]
})
export class AppModule {}
