import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Movie } from './movie';

@Injectable({
  providedIn: 'root'
})
export class MoviesService {
  private readonly API_URL = environment.API_URL;
  constructor(private readonly http: HttpClient) {}

  public getMovies(pageSize = 50, offset = 0): Observable<any> {
    let params = new HttpParams();
    params = params.append('page-size', pageSize.toString());
    params = params.append('offset', offset.toString());
    return this.http.get(`${this.API_URL}/movies`, { params });
  }

  public getMovieById(id: number) {
    return this.http.get(`${this.API_URL}/movies/${id}`);
  }

  public createMovie(data: Partial<Movie>) {
    return this.http.post(`${this.API_URL}/movies`, data);
  }

  public updateMovie(id: number, data: Partial<Movie>) {
    return this.http.patch(`${this.API_URL}/movies/${id}`, data);
  }

  public deleteMovie(id: number) {
    return this.http.delete(`${this.API_URL}/movies/${id}`);
  }
}
