import { Component, OnInit } from '@angular/core';
import {ServiceService} from 'src/app/service.service'
import {profile} from '../../models/profile'
import {cohort} from '../../models/cohort'

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css']
})
export class UserProfileComponent implements OnInit {
  profile!:profile[]
  cohort!:cohort[]
  constructor(private ServiceService:ServiceService) { }
  
  ngOnInit(): void {
    this.Profile()
    this.Cohort()
    
  }
  Profile():void{
    // console.log(this.ServiceService.Profile().subscribe(Profile))
    this.ServiceService.Profile().subscribe(profile=>{
      this.profile=profile
      console.log(profile)
    })
  }
  Cohort():void{
    // console.log(this.ServiceService.Profile().subscribe(Profile))
    this.ServiceService.Cohort().subscribe(cohort=>{
      this.cohort=cohort
      console.log(cohort)
    })
  }
}
