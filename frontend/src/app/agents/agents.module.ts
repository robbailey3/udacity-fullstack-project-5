import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AgentsRootComponent } from './agents-root/agents-root.component';
import { AgentsListComponent } from './agents-list/agents-list.component';
import { AgentsProfileComponent } from './agents-profile/agents-profile.component';
import { HttpClientModule } from '@angular/common/http';
import { AgentCreateComponent } from './agent-create/agent-create.component';
import { AgentEditComponent } from './agent-edit/agent-edit.component';
import { AgentsRoutingModule } from './agents-routing.module';
import { SharedModule } from '../shared/shared.module';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AgentsRootComponent,
    AgentsListComponent,
    AgentsProfileComponent,
    AgentCreateComponent,
    AgentEditComponent
  ],
  imports: [
    CommonModule,
    HttpClientModule,
    AgentsRoutingModule,
    SharedModule,
    FormsModule
  ]
})
export class AgentsModule {}
