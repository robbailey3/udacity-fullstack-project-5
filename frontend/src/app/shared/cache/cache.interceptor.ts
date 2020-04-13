import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpResponse
} from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { CacheService } from './cache.service';
import { filter, map } from 'rxjs/operators';

@Injectable()
export class CacheInterceptor implements HttpInterceptor {
  constructor(private cache: CacheService) {}

  /**
   * A method which is called for all HTTP requests.
   * @param req The request.
   * @param next A function to call to proceed with the request
   * @returns The Observable from the HTTP call or the cached response.
   */
  public intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    if (req.method !== 'GET') {
      /**
       * Only 'GET' requests will produce the same result (they are idempotent) so they
       * are the only ones we can cache.
       */
      return next.handle(req);
    }
    const cachedResponse = this.cache.get(req);
    if (cachedResponse) {
      return of(cachedResponse);
    }

    return next.handle(req).pipe(
      filter((event) => event instanceof HttpResponse),
      map((response: HttpResponse<any>) => {
        this.cache.addToCache(req, response);
        return response;
      })
    );
  }
}
