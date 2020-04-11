import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AgentsRootComponent } from './agents-root/agents-root.component';
import { AgentsListComponent } from './agents-list/agents-list.component';
import { AgentsProfileComponent } from './agents-profile/agents-profile.component';



@NgModule({
  declarations: [AgentsRootComponent, AgentsListComponent, AgentsProfileComponent],
  imports: [
    CommonModule
  ]
})
export class AgentsModule { }
