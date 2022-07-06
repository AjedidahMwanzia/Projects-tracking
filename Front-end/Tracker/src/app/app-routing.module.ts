import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './users/login/login.component';
import { UpdateProfileComponent } from './users/update-profile/update-profile.component';
import { UserProfileComponent } from './users/user-profile/user-profile.component';

const routes: Routes = [
  {path:'login', component:LoginComponent},
  {path:'my-profile',component:UserProfileComponent},
  {path:'update-profile',component:UpdateProfileComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
// array of all routing components
export const routingComponents = [LoginComponent,UserProfileComponent]