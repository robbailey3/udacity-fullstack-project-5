import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AgentsRootComponent } from './agents-root/agents-root.component';
import { AgentsListComponent } from './agents-list/agents-list.component';
import { AgentsProfileComponent } from './agents-profile/agents-profile.component';
import { AgentEditComponent } from './agent-edit/agent-edit.component';
import { AgentCreateComponent } from './agent-create/agent-create.component';

const routes: Routes = [
  {
    path: 'agents',
    component: AgentsRootComponent,
    children: [
      { path: '', pathMatch: 'full', component: AgentsListComponent },
      { path: 'create', component: AgentCreateComponent },
      { path: ':id', component: AgentsProfileComponent },
      { path: ':id/edit', component: AgentEditComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AgentsRoutingModule {}
