import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { timeout } from 'rxjs/operators';

@Injectable()
export class DatabaseService {

  id = null
  name = null

  constructor(private httpClient: HttpClient) {}

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };


  predict(data) {
    data['username'] = this.id
    return this.httpClient.post<Response>('http://localhost:5000/reply', data, this.httpOptions).pipe(
      timeout(10000),
      (res) => {
        return res;
      },
    );
  }
}
