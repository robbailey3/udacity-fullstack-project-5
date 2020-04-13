import { Component, OnInit } from '@angular/core';
import { AgentsService } from '../agents.service';
import { Notification } from '../../shared/notifications/notification';
import { Movie } from 'src/app/movies/movie';
import { Router } from '@angular/router';
import { NotificationService } from 'src/app/shared/notifications/notification.service';
import { MoviesService } from 'src/app/movies/movies.service';
import { Agent } from '../agent';
@Component({
  selector: 'app-agent-create',
  templateUrl: './agent-create.component.html',
  styleUrls: ['./agent-create.component.scss']
})
export class AgentCreateComponent {
  public agent: Partial<Agent> = {};
  constructor(
    private readonly router: Router,
    private readonly agentsService: AgentsService,
    private readonly notificationService: NotificationService
  ) {}

  public submitForm() {
    this.agentsService.createAgent(this.agent).subscribe({
      next: () => {
        this.notificationService.addNotification(
          new Notification('Actor successfully added', 'success')
        );
        this.router.navigateByUrl('/agents');
      },
      error: () => {
        this.notificationService.addNotification(
          new Notification('Something went wrong', 'error')
        );
      }
    });
  }
}
