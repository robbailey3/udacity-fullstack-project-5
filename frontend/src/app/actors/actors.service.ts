import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Actor } from './actor';

@Injectable({
  providedIn: 'root'
})
export class ActorsService {
  private readonly API_URL = environment.API_URL;
  constructor(private readonly http: HttpClient) {}

  public getActors(pageSize = 50, offset = 0): Observable<any> {
    let params = new HttpParams();
    params = params.append('page-size', pageSize.toString());
    params = params.append('offset', offset.toString());
    return this.http.get(`${this.API_URL}/actors`, { params });
  }

  public getActorByID(id: number) {
    return this.http.get(`${this.API_URL}/actors/${id}`);
  }

  public deleteActor(id: number) {
    return this.http.delete(`${this.API_URL}/actors/${id}`);
  }

  public updateActor(id: number, data: Partial<Actor>) {
    return this.http.patch(`${this.API_URL}/actors/${id}`, data);
  }

  public createActor(data: Partial<Actor>) {
    return this.http.post(`${this.API_URL}/actors`, data);
  }
}
