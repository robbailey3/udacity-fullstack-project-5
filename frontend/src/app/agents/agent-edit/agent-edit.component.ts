import { Component, OnInit } from '@angular/core';
import { Agent } from '../agent';
import { AgentsService } from '../agents.service';
import { Notification } from '../../shared/notifications/notification';
import { ActivatedRoute, Router, Params } from '@angular/router';
import { NotificationService } from 'src/app/shared/notifications/notification.service';
import { MoviesService } from 'src/app/movies/movies.service';

@Component({
  selector: 'app-agent-edit',
  templateUrl: './agent-edit.component.html',
  styleUrls: ['./agent-edit.component.scss']
})
export class AgentEditComponent implements OnInit {
  public agent: Partial<Agent> = {};
  public id: number;
  constructor(
    private readonly route: ActivatedRoute,
    private readonly router: Router,
    private readonly agentsService: AgentsService,
    private readonly notificationService: NotificationService
  ) {}

  public ngOnInit(): void {
    this.getIdFromRoute();
  }

  public getIdFromRoute() {
    this.route.paramMap.subscribe((params: Params) => {
      this.id = params.get('id');
      this.getData();
    });
  }

  public getData() {
    this.agentsService.getAgentById(this.id).subscribe({
      next: (res: any) => {
        this.agent = res.result;
        console.log(this);
      }
    });
  }

  public submitForm() {
    this.agentsService.updateAgent(this.id, this.agent).subscribe({
      next: () => {
        this.notificationService.addNotification(
          new Notification('Movie successfully added', 'success')
        );
        this.router.navigateByUrl('/actors');
      },
      error: () => {
        this.notificationService.addNotification(
          new Notification('Something went wrong', 'error')
        );
      }
    });
  }
}
