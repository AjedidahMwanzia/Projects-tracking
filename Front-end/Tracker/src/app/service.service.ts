import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable, observable } from 'rxjs';
import {HttpClient} from '@angular/common/http'
import { profile } from './models/profile';
import { projects } from './models/project';
import { cohort } from './models/cohort';



@Injectable({
  providedIn: 'root'
})
export class ServiceService {
API_URL=environment.API_URL

  constructor(private http:HttpClient) { }

  Profile():Observable<profile[]>{
    return this.http.get<profile[]>(`${this.API_URL}/profile`);
  }
  Projects():Observable<projects[]>{
    return this.http.get<projects[]>(`${this.API_URL}/projects`)
}
  Cohort():Observable<cohort[]>{
    return this.http.get<cohort[]>(`${this.API_URL}/cohort`)
  }
}