import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CacheService } from './cache.service';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { CacheInterceptor } from './cache.interceptor';

@NgModule({
  declarations: [],
  providers: [
    CacheService,
    { provide: HTTP_INTERCEPTORS, useClass: CacheInterceptor, multi: true }
  ],
  imports: [CommonModule]
})
export class CacheModule {}
