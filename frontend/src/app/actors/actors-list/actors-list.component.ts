import { Component, OnInit } from '@angular/core';
import { ActorsService } from '../actors.service';
import { Actor } from '../actor';
import { AuthService } from '../../auth/auth.service';
import { NotificationService } from '../../shared/notifications/notification.service';
import { Notification } from '../../shared/notifications/notification';

@Component({
  selector: 'app-actors-list',
  templateUrl: './actors-list.component.html',
  styleUrls: ['./actors-list.component.scss']
})
export class ActorsListComponent implements OnInit {
  public actors: Actor[];
  public pageSize = 50;
  public offset = 0;
  constructor(
    private readonly actorsService: ActorsService,
    public readonly authService: AuthService,
    private readonly notificationService: NotificationService
  ) {}

  public ngOnInit(): void {
    this.getData();
  }

  public getData() {
    this.actorsService
      .getActors()
      .subscribe({ next: (res) => (this.actors = res.result) });
  }

  public deleteActor(actorID: number) {
    this.actorsService.deleteActor(actorID).subscribe({
      next: () => {
        this.notificationService.addNotification(
          new Notification(`Actor ID ${actorID} deleted`, 'success')
        );
      },
      error: () => {
        this.notificationService.addNotification(
          new Notification('Something went wrong', 'error')
        );
      }
    });
  }
}
'';
