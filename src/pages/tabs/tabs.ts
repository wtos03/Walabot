import { Component } from '@angular/core';

import { SetPage } from '../set/set';
import { ConfigPage } from '../config/config';
import { ActionPage } from '../action/action';

@Component({
  templateUrl: 'tabs.html'
})
export class TabsPage {

  tab1Root = ConfigPage;
  tab2Root = ActionPage;
  tab3Root = SetPage;

  constructor() {

  }
}
