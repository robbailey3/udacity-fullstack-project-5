import { Component, OnInit } from '@angular/core';
import { AgentsService } from '../agents.service';
import { Agent } from '../agent';

@Component({
  selector: 'app-agents-list',
  templateUrl: './agents-list.component.html',
  styleUrls: ['./agents-list.component.scss']
})
export class AgentsListComponent implements OnInit {
  public agents: Agent[];
  constructor(private readonly agentService: AgentsService) {}

  ngOnInit(): void {
    this.getData();
  }

  public getData() {
    this.agentService
      .getAgents()
      .subscribe({ next: (res) => (this.agents = res.result) });
  }
}
