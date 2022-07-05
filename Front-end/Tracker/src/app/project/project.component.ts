import { Component, OnInit } from '@angular/core';
import {ServiceService} from 'src/app/service.service'
import {project} from '../models/project'

@Component({
  selector: 'app-project',
  templateUrl: './project.component.html',
  styleUrls: ['./project.component.css']
})
export class ProjectComponent implements OnInit {
  project!:project[]
  constructor(private ServiceService:ServiceService) { }

  ngOnInit(): void {
    this.Project()
  }

  Project():void{
    this.ServiceService.Project().subscribe(project=>{
      this.project=project
      console.log(project)
    })
  }
}
