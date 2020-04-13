import { HttpResponse, HttpParams } from '@angular/common/http';

export interface CacheEntry {
  response: HttpResponse<any>;
  expiry: number;
  params: HttpParams;
}
