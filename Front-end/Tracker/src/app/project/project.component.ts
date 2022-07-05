import { Component, OnInit } from '@angular/core';
import {ServiceService} from 'src/app/service.service'
import {projects} from '../models/project'

@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.css']
})
export class ProjectComponent implements OnInit {
  projects!:projects[]
  constructor(private ServiceService:ServiceService) { }

  ngOnInit(): void {
    this.Projects()
  }

  Projects():void{
    this.ServiceService.Projects().subscribe(projects=>{
      this.projects=projects
      // console.log(projects)
    })
  }
}
