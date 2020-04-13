import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Agent } from './agent';

@Injectable({
  providedIn: 'root'
})
export class AgentsService {
  private readonly API_URL = environment.API_URL;
  constructor(private readonly http: HttpClient) {}

  public getAgents(pageSize = 50, offset = 0): Observable<any> {
    let params = new HttpParams();
    params = params.append('page-size', pageSize.toString());
    params = params.append('offset', offset.toString());
    return this.http.get(`${this.API_URL}/agents`, { params });
  }

  public getAgentById(id: number) {
    return this.http.get(`${this.API_URL}/agents/${id}`);
  }
  public updateAgent(id: number, data: Partial<Agent>) {
    return this.http.patch(`${this.API_URL}/agents/${id}`, data);
  }
  public createAgent(data: Partial<Agent>) {
    return this.http.post(`${this.API_URL}/agents`, data);
  }
  public deleteAgent(id: number) {
    return this.http.delete(`${this.API_URL}/agents/${id}`);
  }
}
